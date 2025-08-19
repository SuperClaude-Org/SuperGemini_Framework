"""
SuperGemini Installation Operation Module
Refactored from install.py for unified CLI hub
"""

import sys
import time
from pathlib import Path
from typing import List, Optional, Dict, Any
import argparse

from ...core.installer import Installer
from ...core.registry import ComponentRegistry
from ...services.config import ConfigService
from ...core.validator import Validator
from ...utils.ui import (
    display_header, display_info, display_success, display_error, 
    display_warning, Menu, confirm, ProgressBar, Colors, format_size, prompt_api_key
)
from ...utils.environment import setup_environment_variables
from ...utils.logger import get_logger
from ...utils.paths import get_safe_components_directory
from ... import DEFAULT_INSTALL_DIR, PROJECT_ROOT, DATA_DIR
from ..base import OperationBase


class InstallOperation(OperationBase):
    """Installation operation implementation"""
    
    def __init__(self):
        super().__init__("install")


def register_parser(subparsers, global_parser=None) -> argparse.ArgumentParser:
    """Register installation CLI arguments"""
    parents = [global_parser] if global_parser else []
    
    parser = subparsers.add_parser(
        "install",
        help="Install SuperGemini framework components",
        description="Install SuperGemini Framework with various options and profiles",
        epilog="""
Examples:
  SuperGemini install                          # Interactive installation
  SuperGemini install --dry-run                # Dry-run mode  
  SuperGemini install --components core mcp    # Specific components
  SuperGemini install --verbose --force        # Verbose with force mode
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=parents
    )
    
    # Component selection
    parser.add_argument(
        "--components", "-c",
        nargs="+",
        choices=["core", "mcp", "modes", "commands", "agents", "mcp_docs"],
        help="Specific components to install (default: interactive selection)"
    )
    
    # MCP Server selection
    parser.add_argument(
        "--mcp-servers", "--mcp",
        nargs="+",
        choices=["context7", "sequential", "magic", "playwright", "serena", "morphllm", "semantic-prompt"],
        help="MCP servers to configure (default: interactive selection)"
    )
    
    # Installation profiles
    parser.add_argument(
        "--profile", "-p",
        choices=["minimal", "standard", "full", "custom"],
        default="standard",
        help="Installation profile (default: standard)"
    )
    
    # Force overwrite options
    parser.add_argument(
        "--force-overwrite",
        action="store_true",
        help="Force overwrite of existing files"
    )
    
    parser.add_argument(
        "--skip-validation",
        action="store_true", 
        help="Skip post-installation validation"
    )

    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip backup creation during installation"
    )

    parser.add_argument(
        "--skip-gemini-md",
        action="store_true",
        help="Skip GEMINI.md management during installation"
    )
    
    parser.set_defaults(func=run_install)
    return parser


def get_components_to_install(args: argparse.Namespace, registry: ComponentRegistry, config_manager: ConfigService) -> Optional[List[str]]:
    """
    Determine which components to install based on arguments and user input.
    
    Args:
        args: Command line arguments
        registry: Component registry
        config_manager: Configuration manager
        
    Returns:
        List of component names to install, or None if cancelled
    """
    logger = get_logger()
    
    # Check if components specified via command line
    if hasattr(args, 'components') and args.components:
        logger.info(f"Using command-line specified components: {args.components}")
        return args.components
    
    # Interactive selection
    logger.info("Starting interactive component selection...")
    components = interactive_component_selection(registry, config_manager)
    
    if components is None:
        logger.info("Installation cancelled by user during component selection")
        return None
    
    return components


def handle_existing_installation(install_dir: Path, args: argparse.Namespace) -> bool:
    """
    Handle case where installation directory already exists.
    
    Args:
        install_dir: Installation directory path
        args: Command line arguments
        
    Returns:
        True to continue, False to cancel
    """
    logger = get_logger()
    
    if not install_dir.exists():
        return True
        
    # Check if forced
    if args.force:
        logger.info("Continuing with existing installation (--force specified)")
        return True
        
    # Interactive confirmation
    display_warning(f"Installation directory already exists: {install_dir}")
    
    if args.yes or confirm("Continue and update existing installation?"):
        return True
    else:
        display_info("Installation cancelled by user")
        return False


def validate_prerequisites(args: argparse.Namespace) -> bool:
    """
    Validate system prerequisites for installation.
    
    Args:
        args: Command line arguments
        
    Returns:
        True if all prerequisites met, False otherwise
    """
    logger = get_logger()
    logger.info("Validating system requirements...")
    
    try:
        validator = Validator()
        
        # Check Python version
        if not validator.check_python_version():
            display_error("Python version requirements not met")
            return False
            
        # Check disk space
        if not validator.check_disk_space(args.install_dir):
            display_error("Insufficient disk space")
            return False
            
        # Check permissions
        if not validator.check_write_permissions(args.install_dir):
            display_error(f"No write permissions for {args.install_dir}")
            return False
            
        display_success("All system requirements met")
        return True
        
    except Exception as e:
        logger.error(f"Prerequisites validation failed: {e}")
        display_error(f"Prerequisites validation failed: {e}")
        return False


def setup_install_environment(args: argparse.Namespace) -> bool:
    """
    Setup environment variables and paths for installation.
    
    Args:
        args: Command line arguments
        
    Returns:
        True if setup successful, False otherwise  
    """
    logger = get_logger()
    
    try:
        # Setup environment variables
        env_vars = setup_environment_variables(args.install_dir)
        logger.debug(f"Environment variables set: {list(env_vars.keys())}")
        
        # Ensure install directory exists
        args.install_dir.mkdir(parents=True, exist_ok=True)
        
        return True
        
    except Exception as e:
        logger.error(f"Environment setup failed: {e}")
        display_error(f"Environment setup failed: {e}")
        return False


def select_mcp_servers(registry: ComponentRegistry) -> List[str]:
    """
    Interactive MCP server selection.
    
    Args:
        registry: Component registry
        
    Returns:
        List of selected MCP server names
    """
    logger = get_logger()
    
    display_info("\n" + "═" * 63)
    display_info("Stage 1: MCP Server Selection (Optional)")
    display_info("═" * 63)
    display_info("")
    display_info("MCP servers extend Gemini CLI with specialized capabilities.")
    display_info("Select servers to configure (you can always add more later):")
    display_info("")
    
    # MCP server options with descriptions
    mcp_options = [
        ("context7", "Official library documentation and code examples"),
        ("sequential", "Multi-step problem solving and systematic analysis"),
        ("magic", "Modern UI component generation and design systems (requires API key)"),
        ("playwright", "Cross-browser E2E testing and automation"),
        ("serena", "Semantic code analysis and intelligent editing"),
        ("morphllm", "Fast Apply capability for context-aware code modifications (requires API key)"),
        ("semantic-prompt", "Intelligent prompt enhancement and chain-of-thought reasoning"),
        ("Skip MCP Server installation", "")
    ]
    
    print("Select MCP servers to configure:")
    print("================================")
    for i, (name, desc) in enumerate(mcp_options, 1):
        display_text = f"{name} - {desc}" if desc else name
        print(f" {i}. [ ] {display_text}")
    
    print("\nEnter numbers separated by commas (e.g., 1,3,5) or 'all' for all options: ")
    
    try:
        user_input = input("> ").strip().lower()
        
        if not user_input:
            display_info("EOF detected, cancelling operation.")
            logger.info("No MCP servers selected")
            return []
        
        # Handle 'all' option
        if user_input == 'all':
            selected = [opt[0] for opt in mcp_options[:-1]]  # Exclude "Skip" option
            logger.info(f"Selected all MCP servers: {selected}")
            return selected
        
        # Handle skip option
        if user_input in ['8', 'skip']:
            logger.info("No MCP servers selected")
            return []
        
        # Parse selection
        selected_indices = []
        for item in user_input.replace(',', ' ').split():
            try:
                idx = int(item) - 1
                if 0 <= idx < len(mcp_options) - 1:  # Exclude "Skip" option
                    selected_indices.append(idx)
                elif idx == len(mcp_options) - 1:  # Skip option
                    logger.info("No MCP servers selected")
                    return []
            except ValueError:
                continue
        
        selected = [mcp_options[i][0] for i in selected_indices]
        logger.info(f"Selected MCP servers: {selected}")
        return selected
        
    except (EOFError, KeyboardInterrupt):
        display_info("EOF detected, cancelling operation.")
        logger.info("No MCP servers selected")
        return []


def select_framework_components(registry: ComponentRegistry, config_manager: ConfigService, selected_mcp_servers: List[str]) -> List[str]:
    """
    Interactive framework component selection.
    
    Args:
        registry: Component registry  
        config_manager: Configuration manager
        selected_mcp_servers: Previously selected MCP servers
        
    Returns:
        List of selected component names
    """
    logger = get_logger()
    
    display_info("\n" + "═" * 63)
    display_info("Stage 2: Framework Component Selection")
    display_info("═" * 63)
    display_info("")
    
    # Get available components
    available_components = registry.list_components()
    
    # Prepare component options with descriptions
    component_options = []
    for comp_name in ["core", "modes", "commands", "agents", "mcp_docs"]:
        if comp_name in available_components:
            metadata = registry.get_component_metadata(comp_name)
            if metadata:
                desc = metadata.get("description", "No description available")
                
                # Special handling for mcp_docs
                if comp_name == "mcp_docs":
                    if selected_mcp_servers:
                        desc = f"MCP documentation for {', '.join(selected_mcp_servers)}"
                    else:
                        desc = "MCP server documentation (none selected)"
                
                component_options.append((comp_name, desc))
    
    if not component_options:
        display_error("No components available for installation")
        return []
    
    display_info("Select components (Core is recommended):")
    display_info("=" * 40)
    
    for i, (name, desc) in enumerate(component_options, 1):
        print(f" {i}. [ ] {name} - {desc}")
    
    print("\nEnter numbers separated by commas (e.g., 1,3,5) or 'all' for all options: ")
    try:
        user_input = input("> ").strip().lower()
        
        if not user_input:
            display_info("EOF detected, cancelling operation.")
            logger.info("No components selected, defaulting to core")
            return ["core"]
        
        # Handle 'all' option
        if user_input == 'all':
            selected = [opt[0] for opt in component_options]
            logger.info(f"Selected all components: {selected}")
            return selected
        
        # Parse selection
        selected_indices = []
        for item in user_input.replace(',', ' ').split():
            try:
                idx = int(item) - 1
                if 0 <= idx < len(component_options):
                    selected_indices.append(idx)
            except ValueError:
                continue
        
        if not selected_indices:
            logger.info("No valid selection, defaulting to core")
            return ["core"]
        
        selected = [component_options[i][0] for i in selected_indices]
        logger.info(f"Selected framework components: {selected}")
        return selected
        
    except (EOFError, KeyboardInterrupt):
        display_info("EOF detected, cancelling operation.")
        logger.info("No components selected, defaulting to core")
        return ["core"]


def interactive_component_selection(registry: ComponentRegistry, config_manager: ConfigService) -> Optional[List[str]]:
    """
    Interactive component selection workflow.
    
    Args:
        registry: Component registry
        config_manager: Configuration manager
        
    Returns:
        List of selected components, or None if cancelled
    """
    logger = get_logger()
    
    # Stage 1: MCP Server Selection
    selected_mcp_servers = select_mcp_servers(registry)
    
    # Stage 2: Framework Component Selection  
    selected_components = select_framework_components(registry, config_manager, selected_mcp_servers)
    
    # Auto-add MCP component if MCP servers were selected
    if selected_mcp_servers and "mcp" not in selected_components:
        selected_components.append("mcp")
        logger.info("Auto-selected MCP component for configured servers")
    
    # Auto-add mcp_docs if MCP servers were selected
    if selected_mcp_servers and "mcp_docs" not in selected_components:
        selected_components.append("mcp_docs")
        logger.info("Auto-selected MCP documentation for configured servers")
    
    if selected_components:
        logger.info(f"Final selection: {selected_components}")
    
    return selected_components


def display_installation_plan(components: List[str], registry: ComponentRegistry, install_dir: Path) -> None:
    """
    Display installation plan to user.
    
    Args:
        components: List of components to install
        registry: Component registry
        install_dir: Installation directory
    """
    display_info("\nInstallation Plan")
    display_info("=" * 50)
    display_info(f"Installation Directory: {install_dir}")
    display_info("Components to install:")
    
    total_size = 0
    for i, comp_name in enumerate(components, 1):
        metadata = registry.get_component_metadata(comp_name)
        if metadata:
            desc = metadata.get("description", "No description available")
            display_info(f"  {i}. {comp_name} - {desc}")
            
            # Try to get size estimate if component supports it
            try:
                instance = registry.get_component_instance(comp_name, install_dir)
                if instance and hasattr(instance, 'get_size_estimate'):
                    size = instance.get_size_estimate()
                    total_size += size
            except Exception:
                pass
    
    if total_size > 0:
        display_info(f"\nEstimated size: {format_size(total_size)}")


def execute_installation(components: List[str], installer: Installer, registry: ComponentRegistry, 
                        component_instances: Dict[str, Any], args: argparse.Namespace) -> bool:
    """
    Execute the actual installation process.
    
    Args:
        components: List of component names to install
        installer: Installer instance
        registry: Component registry
        component_instances: Component instances
        args: Command line arguments
        
    Returns:
        True if installation successful, False otherwise
    """
    logger = get_logger()
    
    try:
        # Create backup if not disabled
        if not args.no_backup:
            logger.info("Creating backup of existing installation...")
            backup_path = installer.create_backup()
            if backup_path:
                logger.info(f"Backup created: {backup_path}")
        
        # Execute installation
        logger.info(f"Installing {len(components)} components...")
        
        # Setup progress bar
        progress = ProgressBar(len(components), prefix="Installing")
        
        installed_components = []
        
        for i, component_name in enumerate(components):
            instance = component_instances.get(component_name)
            if not instance:
                logger.warning(f"No instance available for component: {component_name}")
                continue
            
            logger.info(f"Installing {component_name}...")
            
            # Install component
            config = {
                "force_overwrite": args.force_overwrite,
                "skip_gemini_md": args.skip_gemini_md,
                "dry_run": args.dry_run
            }
            
            # Add MCP server selection if installing MCP component
            if component_name == "mcp" and hasattr(args, "mcp_servers") and args.mcp_servers:
                config["selected_mcp_servers"] = args.mcp_servers
                logger.info(f"Configuring MCP servers: {args.mcp_servers}")
            
            success = instance.install(config)
            
            if success:
                installed_components.append(component_name)
                logger.info(f"✓ {instance} component installed successfully")
            else:
                logger.error(f"✗ Failed to install component: {component_name}")
                display_error(f"Failed to install component: {component_name}")
                
                # Continue with remaining components
                continue
            
            progress.update(i + 1)
        
        progress.finish()
        
        if not installed_components:
            logger.error("No components were installed successfully")
            return False
        
        # Post-installation validation
        if not args.skip_validation:
            logger.info("Running post-installation validation...")
            validation_success = True
            
            for component_name in installed_components:
                instance = component_instances.get(component_name)
                if instance:
                    is_valid, errors = instance.validate_installation()
                    if is_valid:
                        logger.info(f"  ✓ {component_name}: Valid")
                    else:
                        logger.warning(f"  ✗ {component_name}: {', '.join(errors)}")
                        validation_success = False
            
            if validation_success:
                logger.info("All components validated successfully!")
            else:
                logger.warning("Some components failed validation")
        
        logger.info(f"Installed components: {', '.join(installed_components)}")
        return True
        
    except Exception as e:
        logger.exception(f"Installation execution failed: {e}")
        display_error(f"Installation failed: {e}")
        return False


def run_install(args: argparse.Namespace) -> bool:
    """
    Execute SuperGemini installation operation.
    
    Args:
        args: Command line arguments
        
    Returns:
        True if installation successful, False otherwise
    """
    logger = get_logger()
    logger.info("Executing operation: install")
    logger.info("Starting install operation")
    
    # Security validation
    from ...utils.security import SecurityValidator
    security = SecurityValidator()
    if not security.validate_gemini_directory_installation(args.install_dir):
        display_error("Security validation failed for installation directory")
        return False
    
    # Display header
    display_header("SuperGemini Installation v4.0.4", 
                  "Installing SuperGemini framework components")
    
    # Handle existing installation
    if not handle_existing_installation(args.install_dir, args):
        return False
    
    # Validate prerequisites  
    if not validate_prerequisites(args):
        return False
        
    # Setup environment
    if not setup_install_environment(args):
        return False
        
    logger.info("Initializing installation system...")
    
    # Use validate_and_install to handle component selection and installation
    return validate_and_install(args)


def install_with_profile(args: argparse.Namespace) -> bool:
    """
    Install SuperGemini with a predefined profile.
    
    Args:
        args: Command line arguments with profile specified
        
    Returns:
        True if installation successful, False otherwise
    """
    logger = get_logger()
    
    profile_components = {
        "minimal": ["core"],
        "standard": ["core", "modes", "commands"],
        "full": ["core", "modes", "commands", "agents", "mcp"],
        "custom": None  # Will use interactive selection
    }
    
    if args.profile == "custom":
        logger.info("Using custom profile - falling back to interactive selection")
        # Get registry for custom selection
        try:
            components_dir = get_safe_components_directory()
            registry = ComponentRegistry(components_dir)
            registry.discover_components()
        except FileNotFoundError as e:
            logger.error(f"Component discovery failed: {e}")
            display_error(f"Cannot locate components: {e}")
            return False
        
        config_manager = ConfigService(args.install_dir)
        components = get_components_to_install(args, registry, config_manager)
        if components is None:
            return False
    else:
        components = profile_components.get(args.profile, ["core"])
        logger.info(f"Installing with {args.profile} profile: {components}")
        
        # Get registry for installation
        try:
            components_dir = get_safe_components_directory()
            registry = ComponentRegistry(components_dir)
            registry.discover_components()
        except FileNotFoundError as e:
            logger.error(f"Component discovery failed: {e}")
            display_error(f"Cannot locate components: {e}")
            return False
        
        # If full profile and MCP component included, set default MCP servers
        if args.profile == "full" and "mcp" in components:
            if not hasattr(args, 'mcp_servers') or not args.mcp_servers:
                # Set default MCP servers for full installation (all servers)
                # serena and morphllm will be automatically installed as disabled
                args.mcp_servers = ["semantic-prompt", "sequential", "context7", "magic", "serena", "morphllm", "playwright"]
                logger.info(f"Full installation - automatically including all MCP servers: {args.mcp_servers}")
    
    # Run the actual installation
    return execute_install_workflow(args, components, registry)


def validate_and_install(args: argparse.Namespace) -> bool:
    """
    Validate arguments and run installation.
    
    Args:
        args: Command line arguments
        
    Returns:
        True if installation successful, False otherwise
    """
    logger = get_logger()
    
    try:
        # Create component registry to validate component names
        try:
            components_dir = get_safe_components_directory()
            registry = ComponentRegistry(components_dir)
            registry.discover_components()
        except FileNotFoundError as e:
            logger.error(f"Component validation failed: {e}")
            display_error(f"Cannot validate components: {e}")
            return False
        
        available_components = registry.list_components()
        
        # Validate specified components
        if hasattr(args, 'components') and args.components:
            invalid_components = [c for c in args.components if c not in available_components]
            if invalid_components:
                display_error(f"Invalid components specified: {invalid_components}")
                display_info(f"Available components: {available_components}")
                return False
        
        # If no components specified and using standard profile, automatically use full installation
        if (not hasattr(args, 'components') or not args.components) and args.profile == "standard":
            args.profile = "full"
            logger.info("No components specified - using full installation profile")
            return install_with_profile(args)
        
        # Install with profile if specified
        if args.profile != "standard":
            return install_with_profile(args)
        
        # Standard installation - DO NOT call run_install here to avoid recursion
        # Just determine components and continue
        config_manager = ConfigService(args.install_dir)
        components = get_components_to_install(args, registry, config_manager)
        if components is None:
            return False
            
        # Run the actual installation
        return execute_install_workflow(args, components, registry)
        
    except Exception as e:
        logger.exception(f"Validation and installation failed: {e}")
        display_error(f"Installation failed: {e}")
        return False


# Components determination
def determine_components_to_install(args: argparse.Namespace) -> Optional[List[str]]:
    """
    Determine components to install based on arguments.
    
    Args:
        args: Command line arguments
        
    Returns:
        List of component names, or None if cancelled
    """
    logger = get_logger()
    
    try:
        # Create registry to get available components
        try:
            components_dir = get_safe_components_directory()
            registry = ComponentRegistry(components_dir)
            registry.discover_components()
        except FileNotFoundError as e:
            logger.error(f"Component discovery failed: {e}")
            return None
        
        # Create config manager
        config_manager = ConfigService(args.install_dir)
        
        # Get components to install
        components = get_components_to_install(args, registry, config_manager)
        
        if components is None:
            return None
            
        # Resolve dependencies
        try:
            resolved_components = registry.resolve_dependencies(components, args.install_dir)
            logger.info(f"Resolved component dependencies: {resolved_components}")
            return resolved_components
        except ValueError as e:
            logger.error(f"Dependency resolution failed: {e}")
            display_error(f"Component dependency error: {e}")
            return None
            
    except Exception as e:
        logger.exception(f"Component determination failed: {e}")
        return None


def execute_install_workflow(args: argparse.Namespace, components: List[str], registry: ComponentRegistry) -> bool:
    """
    Execute the actual installation workflow
    
    Args:
        args: Command line arguments
        components: List of components to install
        registry: Component registry instance
        
    Returns:
        True if installation successful, False otherwise
    """
    logger = get_logger()
    
    try:
        # Resolve dependencies
        resolved_components = registry.resolve_dependencies(components)
        logger.info(f"Resolved component dependencies: {resolved_components}")
        
        # Create installer
        installer = Installer(args.install_dir, dry_run=args.dry_run)
        
        # Create component instances
        component_instances = registry.create_component_instances(resolved_components, args.install_dir)
        
        if not component_instances:
            logger.error("No valid component instances created")
            return False
            
        # Display installation plan
        display_installation_plan(resolved_components, registry, args.install_dir)
        
        # Confirm installation
        if not args.dry_run and not args.yes:
            if not confirm("Proceed with installation?"):
                display_info("Installation cancelled by user")
                return False
        
        # Execute installation
        start_time = time.time()
        success = execute_installation(resolved_components, installer, registry, component_instances, args)
        elapsed_time = time.time() - start_time
        
        if success:
            display_success(f"Installation completed successfully in {elapsed_time:.1f} seconds")
            
            # Display next steps
            display_info("\nNext steps:")
            display_info("1. Restart your Gemini CLI session")
            display_info(f"2. Framework files are now available in {args.install_dir}")
            display_info("3. Use SuperGemini commands and features in Gemini CLI")
            
            return True
        else:
            display_error("Installation failed")
            return False
            
    except Exception as e:
        logger.exception(f"Installation workflow failed: {e}")
        display_error(f"Installation failed: {e}")
        return False


def run(args: argparse.Namespace) -> int:
    """Entry point for install operation"""
    try:
        success = validate_and_install(args)
        return 0 if success else 1
    except Exception as e:
        logger = get_logger()
        if logger:
            logger.exception(f"Install operation failed: {e}")
        display_error(f"Install operation failed: {e}")
        return 1