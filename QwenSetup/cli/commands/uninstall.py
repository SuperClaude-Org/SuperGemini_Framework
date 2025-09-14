"""
SuperGemini Uninstall Operation Module
Enhanced complete deletion system with comprehensive file detection
"""

import sys
import time
import json
import re
from pathlib import Path
from typing import List, Optional, Dict, Any, Set, Tuple
import argparse

from ...core.registry import ComponentRegistry
from ...services.settings import SettingsService
from ...services.files import FileService
from ...utils.ui import (
    display_header, display_info, display_success, display_error, 
    display_warning, Menu, confirm, ProgressBar, Colors
)
from ...utils.environment import get_supergemini_environment_variables, cleanup_environment_variables
from ...utils.logger import get_logger
from ... import DEFAULT_INSTALL_DIR, PROJECT_ROOT
from ...utils.paths import get_safe_components_directory
from ..base import OperationBase


class SuperGeminiFileDetector:
    """Enhanced SuperGemini file detection with multiple identification strategies"""
    
    def __init__(self, install_dir: Path):
        self.install_dir = install_dir
        self.logger = get_logger()
        
        # SuperGemini file signatures for content analysis
        self.supergemini_signatures = [
            r'SuperGemini\s+Framework',
            r'SuperClaude\s+Framework',
            r'@FLAGS\.md',
            r'@PRINCIPLES\.md',
            r'@RULES\.md',
            r'MODE_[A-Z][a-z]+\.md',
            r'MCP_[A-Z][a-z]+\.md',
            r'## SuperGemini',
            r'# SuperGemini',
            r'claude.*\.ai/code',
            r'SuperGemini\s+Agent',
            r'SUPERGEMINI_',
            r'framework.*components',
            r'behavioral.*modes',
            r'orchestration.*mode',
            r'token.*efficiency',
            r'mcp.*server',
            r'structured.*thinking',
        ]
        
        # Known SuperGemini file patterns (exact matches)
        self.supergemini_files = {
            # Core framework files
            'CLAUDE.md', 'GEMINI.md', 'FLAGS.md', 'PRINCIPLES.md', 'RULES.md',
            'ORCHESTRATOR.md', 'SESSION_LIFECYCLE.md', 'STRATEGY-MATRIX.md',
            
            # Mode files
            'MODE_Brainstorming.md', 'MODE_Introspection.md', 
            'MODE_Task_Management.md', 'MODE_Token_Efficiency.md',
            'MODE_Orchestration.md',
            
            # MCP documentation
            'MCP_Context7.md', 'MCP_Sequential.md', 'MCP_Magic.md',
            'MCP_Playwright.md', 'MCP_Morphllm.md', 'MCP_Serena.md',
            'MCP_StructuredThinking.md',
        }
        
        # Directory patterns that contain SuperGemini files
        self.supergemini_directories = {
            'commands/sg',
            'agents/supergemini',
            'logs/supergemini',
            'backups/supergemini',
            'metadata/supergemini',
        }

    def is_supergemini_file(self, file_path: Path) -> bool:
        """
        Comprehensive SuperGemini file detection using multiple strategies
        
        Args:
            file_path: Path to file to check
            
        Returns:
            True if file is identified as SuperGemini file
        """
        try:
            # Strategy 1: Exact filename match
            if file_path.name in self.supergemini_files:
                self.logger.debug(f"Exact match: {file_path}")
                return True
            
            # Strategy 2: Directory pattern match
            relative_path = file_path.relative_to(self.install_dir)
            for dir_pattern in self.supergemini_directories:
                if str(relative_path).startswith(dir_pattern):
                    self.logger.debug(f"Directory pattern match: {file_path}")
                    return True
            
            # Strategy 3: Content analysis (for text files)
            if self._is_text_file(file_path):
                if self._analyze_file_content(file_path):
                    self.logger.debug(f"Content analysis match: {file_path}")
                    return True
            
            # Strategy 4: JSON configuration analysis
            if file_path.suffix == '.json' and self._analyze_json_config(file_path):
                self.logger.debug(f"JSON config match: {file_path}")
                return True
            
            # Strategy 5: Log file pattern analysis
            if self._is_supergemini_log(file_path):
                self.logger.debug(f"Log file match: {file_path}")
                return True
                
            return False
            
        except Exception as e:
            self.logger.debug(f"Error analyzing file {file_path}: {e}")
            return False

    def _is_text_file(self, file_path: Path) -> bool:
        """Check if file is a text file suitable for content analysis"""
        try:
            # Check file extension
            text_extensions = {'.md', '.txt', '.json', '.yaml', '.yml', '.toml', '.cfg', '.ini'}
            if file_path.suffix.lower() in text_extensions:
                return True
            
            # Check if file has no extension but might be text
            if not file_path.suffix:
                # Try to read first few bytes
                with open(file_path, 'rb') as f:
                    sample = f.read(512)
                    try:
                        sample.decode('utf-8')
                        return True
                    except UnicodeDecodeError:
                        return False
            
            return False
        except Exception:
            return False

    def _analyze_file_content(self, file_path: Path) -> bool:
        """Analyze file content for SuperGemini signatures"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(4096)  # Read first 4KB only for efficiency
                
                # Check for SuperGemini signatures
                for signature in self.supergemini_signatures:
                    if re.search(signature, content, re.IGNORECASE | re.MULTILINE):
                        return True
                        
            return False
        except Exception:
            return False

    def _analyze_json_config(self, file_path: Path) -> bool:
        """Analyze JSON files for SuperGemini configurations"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Check for SuperGemini-specific configuration keys
                supergemini_keys = [
                    'supergemini', 'SuperGemini', 'mcp_servers', 'structured-thinking',
                    'context7', 'sequential-thinking', 'morphllm', 'serena', 'magic',
                    'playwright-mcp'
                ]
                
                def check_keys(obj, depth=0):
                    if depth > 3:  # Prevent deep recursion
                        return False
                    
                    if isinstance(obj, dict):
                        for key, value in obj.items():
                            if any(sg_key in str(key).lower() for sg_key in supergemini_keys):
                                return True
                            if isinstance(value, (dict, list)):
                                if check_keys(value, depth + 1):
                                    return True
                    elif isinstance(obj, list):
                        for item in obj:
                            if isinstance(item, (dict, list)):
                                if check_keys(item, depth + 1):
                                    return True
                    
                    return False
                
                return check_keys(data)
                
        except Exception:
            return False

    def _is_supergemini_log(self, file_path: Path) -> bool:
        """Check if file is a SuperGemini log file"""
        try:
            # Check log file patterns
            if 'supergemini' in file_path.name.lower():
                return True
            
            # Check if it's in a logs directory and contains SuperGemini references
            if 'logs' in str(file_path).lower():
                if self._analyze_file_content(file_path):
                    return True
            
            return False
        except Exception:
            return False

    def scan_all_files(self) -> Tuple[List[Path], List[Path]]:
        """
        Scan all files in installation directory
        
        Returns:
            Tuple of (supergemini_files, preserved_files)
        """
        supergemini_files = []
        preserved_files = []
        
        if not self.install_dir.exists():
            return supergemini_files, preserved_files
        
        try:
            # Use iterative approach to prevent recursion issues
            dirs_to_scan = [self.install_dir]
            processed_dirs = set()
            
            while dirs_to_scan:
                current_dir = dirs_to_scan.pop(0)
                
                # Prevent infinite loops
                real_path = current_dir.resolve()
                if real_path in processed_dirs:
                    continue
                processed_dirs.add(real_path)
                
                try:
                    for item in current_dir.iterdir():
                        if item.is_file():
                            if self.is_supergemini_file(item):
                                supergemini_files.append(item)
                            else:
                                preserved_files.append(item)
                        elif item.is_dir():
                            # Add to scan queue
                            dirs_to_scan.append(item)
                except PermissionError:
                    self.logger.debug(f"Permission denied: {current_dir}")
                    continue
                    
        except Exception as e:
            self.logger.error(f"Error scanning files: {e}")
        
        return supergemini_files, preserved_files


def verify_supergemini_file(file_path: Path, component: str) -> bool:
    """
    Enhanced SuperGemini file verification
    
    Args:
        file_path: Path to the file to verify
        component: Component name this file belongs to
        
    Returns:
        True if safe to remove, False if uncertain (preserve by default)
    """
    try:
        # Use enhanced detector
        detector = SuperGeminiFileDetector(file_path.parent)
        return detector.is_supergemini_file(file_path)
        
    except Exception:
        # If any error occurs in verification, preserve the file
        return False


def verify_directory_safety(directory: Path, component: str) -> bool:
    """
    Enhanced directory safety verification
    
    Args:
        directory: Directory path to verify
        component: Component name
        
    Returns:
        True if safe to remove (only if empty or only contains SuperGemini files)
    """
    try:
        if not directory.exists():
            return True
        
        # Check if directory is empty
        contents = list(directory.iterdir())
        if not contents:
            return True
        
        # Use enhanced detector for comprehensive analysis
        detector = SuperGeminiFileDetector(directory)
        
        # Check if all contents are SuperGemini files
        for item in contents:
            if item.is_file():
                if not detector.is_supergemini_file(item):
                    return False
            elif item.is_dir():
                # Recursively check subdirectories
                if not verify_directory_safety(item, component):
                    return False
        
        return True
        
    except Exception:
        # If any error occurs, preserve the directory
        return False


class UninstallOperation(OperationBase):
    """Enhanced uninstall operation implementation"""
    
    def __init__(self):
        super().__init__("uninstall")


def register_parser(subparsers, global_parser=None) -> argparse.ArgumentParser:
    """Register uninstall CLI arguments"""
    parents = [global_parser] if global_parser else []
    
    parser = subparsers.add_parser(
        "uninstall",
        help="Remove SuperGemini framework installation",
        description="Uninstall SuperGemini Framework components with complete file detection",
        epilog="""
Examples:
  SuperGemini uninstall                    # Interactive uninstall with enhanced detection
  SuperGemini uninstall --components core  # Remove specific components
  SuperGemini uninstall --complete --force # Complete removal (forced)
  SuperGemini uninstall --keep-backups     # Keep backup files
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=parents
    )
    
    # Uninstall mode options
    parser.add_argument(
        "--components",
        type=str,
        nargs="+",
        help="Specific components to uninstall"
    )
    
    parser.add_argument(
        "--complete",
        action="store_true",
        help="Complete uninstall (remove all SuperGemini files)"
    )
    
    # Data preservation options
    parser.add_argument(
        "--keep-backups",
        action="store_true",
        help="Keep backup files during uninstall"
    )
    
    parser.add_argument(
        "--keep-logs",
        action="store_true",
        help="Keep log files during uninstall"
    )
    
    parser.add_argument(
        "--keep-settings",
        action="store_true",
        help="Keep user settings during uninstall"
    )
    
    # Safety options
    parser.add_argument(
        "--no-confirm",
        action="store_true",
        help="Skip confirmation prompts (use with caution)"
    )
    
    # Environment cleanup options
    parser.add_argument(
        "--cleanup-env",
        action="store_true",
        help="Remove SuperGemini environment variables"
    )
    
    parser.add_argument(
        "--no-restore-script",
        action="store_true",
        help="Skip creating environment variable restore script"
    )
    
    # Enhanced detection options
    parser.add_argument(
        "--verify-all",
        action="store_true",
        help="Verify all files before deletion (slower but safer)"
    )
    
    return parser


def get_installed_components(install_dir: Path) -> Dict[str, Dict[str, Any]]:
    """Get currently installed components with error protection"""
    try:
        from ...services.settings import SettingsService
        settings_manager = SettingsService(install_dir)
        components = settings_manager.get_installed_components()
        
        # Ensure we return a safe dict, preventing recursion
        if isinstance(components, dict):
            return components
        else:
            return {}
    except RecursionError as e:
        # Specifically catch recursion errors
        logger = get_logger()
        logger.error(f"Recursion error in get_installed_components: {e}")
        return {}
    except Exception as e:
        # Log the exception for debugging
        logger = get_logger()
        logger.debug(f"Error getting installed components: {e}")
        return {}


def get_installation_info(install_dir: Path) -> Dict[str, Any]:
    """Get detailed installation information with enhanced file detection"""
    info = {
        "install_dir": install_dir,
        "exists": False,
        "components": {},
        "directories": [],
        "files": [],
        "supergemini_files": [],
        "preserved_files": [],
        "total_size": 0,
        "supergemini_size": 0
    }
    
    if not install_dir.exists():
        return info
    
    info["exists"] = True
    
    try:
        logger = get_logger()
        logger.debug("Getting installed components...")
        info["components"] = get_installed_components(install_dir)
        logger.debug(f"Found components: {list(info['components'].keys())}")
    except Exception as e:
        logger = get_logger()
        logger.error(f"Error getting components in get_installation_info: {e}")
        info["components"] = {}
    
    # Enhanced file scanning with SuperGemini detection
    try:
        detector = SuperGeminiFileDetector(install_dir)
        supergemini_files, preserved_files = detector.scan_all_files()
        
        info["supergemini_files"] = supergemini_files
        info["preserved_files"] = preserved_files
        info["files"] = supergemini_files + preserved_files
        
        # Calculate sizes
        for file_path in supergemini_files:
            try:
                info["supergemini_size"] += file_path.stat().st_size
            except OSError:
                pass
        
        for file_path in preserved_files:
            try:
                info["total_size"] += file_path.stat().st_size
            except OSError:
                pass
        
        info["total_size"] += info["supergemini_size"]
        
        # Find directories
        visited_dirs = set()
        for file_path in info["files"]:
            current_dir = file_path.parent
            while current_dir != install_dir and current_dir not in visited_dirs:
                visited_dirs.add(current_dir)
                info["directories"].append(current_dir)
                current_dir = current_dir.parent
                
    except Exception as e:
        logger = get_logger()
        logger.error(f"Error in enhanced file scanning: {e}")
    
    return info


def display_environment_info() -> Dict[str, str]:
    """Display SuperGemini environment variables and return them"""
    env_vars = get_supergemini_environment_variables()
    
    if env_vars:
        print(f"\n{Colors.CYAN}{Colors.BRIGHT}Environment Variables{Colors.RESET}")
        print("=" * 50)
        print(f"{Colors.BLUE}SuperGemini API key environment variables found:{Colors.RESET}")
        for env_var, value in env_vars.items():
            # Show only first few and last few characters for security
            masked_value = f"{value[:4]}...{value[-4:]}" if len(value) > 8 else "***"
            print(f"  {env_var}: {masked_value}")
        
        print(f"\n{Colors.YELLOW}Note: These environment variables will remain unless you use --cleanup-env{Colors.RESET}")
    else:
        print(f"\n{Colors.GREEN}No SuperGemini environment variables found{Colors.RESET}")
    
    return env_vars


def display_uninstall_info(info: Dict[str, Any]) -> None:
    """Display enhanced installation information before uninstall"""
    print(f"\n{Colors.CYAN}{Colors.BRIGHT}Current Installation Analysis{Colors.RESET}")
    print("=" * 50)
    
    if not info["exists"]:
        print(f"{Colors.YELLOW}No SuperGemini installation found{Colors.RESET}")
        return
    
    print(f"{Colors.BLUE}Installation Directory:{Colors.RESET} {info['install_dir']}")
    
    if info["components"]:
        print(f"{Colors.BLUE}Installed Components:{Colors.RESET}")
        for component, version in info["components"].items():
            if isinstance(version, dict):
                version_str = version.get('version', 'unknown')
            else:
                version_str = str(version)
            print(f"  {component}: v{version_str}")
    
    # Enhanced file information
    supergemini_count = len(info.get("supergemini_files", []))
    preserved_count = len(info.get("preserved_files", []))
    
    print(f"{Colors.BLUE}File Analysis:{Colors.RESET}")
    print(f"  SuperGemini files: {Colors.RED}{supergemini_count}{Colors.RESET} (will be removed)")
    print(f"  Preserved files: {Colors.GREEN}{preserved_count}{Colors.RESET} (will be kept)")
    print(f"  Directories: {len(info['directories'])}")
    
    if info["total_size"] > 0:
        from ...utils.ui import format_size
        supergemini_size = info.get("supergemini_size", 0)
        print(f"{Colors.BLUE}Size Analysis:{Colors.RESET}")
        print(f"  SuperGemini data: {Colors.RED}{format_size(supergemini_size)}{Colors.RESET}")
        print(f"  Total installation: {format_size(info['total_size'])}")
    
    print()


def get_components_to_uninstall(args: argparse.Namespace, installed_components: Dict[str, str]) -> Optional[List[str]]:
    """Determine which components to uninstall"""
    logger = get_logger()
    
    # Complete uninstall
    if args.complete:
        return list(installed_components.keys())
    
    # Explicit components specified
    if args.components:
        # Validate that specified components are installed
        invalid_components = [c for c in args.components if c not in installed_components]
        if invalid_components:
            logger.error(f"Components not installed: {invalid_components}")
            return None
        return args.components
    
    # Interactive selection
    return interactive_uninstall_selection(installed_components)


def interactive_component_selection(installed_components: Dict[str, str], env_vars: Dict[str, str]) -> Optional[tuple]:
    """
    Enhanced interactive selection with granular component options
    
    Returns:
        Tuple of (components_to_remove, cleanup_options) or None if cancelled
    """
    if not installed_components:
        return []
    
    print(f"\n{Colors.CYAN}{Colors.BRIGHT}SuperGemini Uninstall Options{Colors.RESET}")
    print("=" * 60)
    
    # Main uninstall type selection
    main_options = [
        "Complete Uninstall (remove all SuperGemini components)",
        "Custom Uninstall (choose specific components)",
        "Cancel Uninstall"
    ]
    
    print(f"\n{Colors.BLUE}Choose uninstall type:{Colors.RESET}")
    main_menu = Menu("Select option:", main_options)
    main_choice = main_menu.display()
    
    if main_choice == -1 or main_choice == 2:  # Cancelled
        return None
    elif main_choice == 0:  # Complete uninstall
        # Complete uninstall - include all components and optional cleanup
        cleanup_options = _ask_complete_uninstall_options(env_vars)
        return list(installed_components.keys()), cleanup_options
    elif main_choice == 1:  # Custom uninstall
        return _custom_component_selection(installed_components, env_vars)
    
    return None


def _ask_complete_uninstall_options(env_vars: Dict[str, str]) -> Dict[str, bool]:
    """Ask for complete uninstall options"""
    cleanup_options = {
        'remove_mcp_configs': True,
        'cleanup_env_vars': False,
        'create_restore_script': True
    }
    
    print(f"\n{Colors.YELLOW}{Colors.BRIGHT}Complete Uninstall Options{Colors.RESET}")
    print("This will remove ALL SuperGemini components.")
    
    if env_vars:
        print(f"\n{Colors.BLUE}Environment variables found:{Colors.RESET}")
        for env_var, value in env_vars.items():
            masked_value = f"{value[:4]}...{value[-4:]}" if len(value) > 8 else "***"
            print(f"  {env_var}: {masked_value}")
        
        cleanup_env = confirm("Also remove API key environment variables?", default=False)
        cleanup_options['cleanup_env_vars'] = cleanup_env
        
        if cleanup_env:
            create_script = confirm("Create restore script for environment variables?", default=True)
            cleanup_options['create_restore_script'] = create_script
    
    return cleanup_options


def _custom_component_selection(installed_components: Dict[str, str], env_vars: Dict[str, str]) -> Optional[tuple]:
    """Handle custom component selection with granular options"""
    print(f"\n{Colors.CYAN}{Colors.BRIGHT}Custom Uninstall - Choose Components{Colors.RESET}")
    print("Select which SuperGemini components to remove:")
    
    # Build component options with descriptions
    component_options = []
    component_keys = []
    
    component_descriptions = {
        'core': 'Core Framework Files (GEMINI.md, FLAGS.md, PRINCIPLES.md, etc.)',
        'commands': 'SuperGemini Commands (commands/sg/*.md)',
        'mcp': 'MCP Server Configurations',
        'mcp_docs': 'MCP Documentation',
        'modes': 'SuperGemini Modes'
    }
    
    for component, version in installed_components.items():
        description = component_descriptions.get(component, f"{component} component")
        component_options.append(f"{description}")
        component_keys.append(component)
    
    print(f"\n{Colors.BLUE}Select components to remove:{Colors.RESET}")
    component_menu = Menu("Components:", component_options, multi_select=True)
    selections = component_menu.display()
    
    if not selections:
        return None
    
    selected_components = [component_keys[i] for i in selections]
    
    # If MCP component is selected, ask about related cleanup options
    cleanup_options = {
        'remove_mcp_configs': 'mcp' in selected_components,
        'cleanup_env_vars': False,
        'create_restore_script': True
    }
    
    if 'mcp' in selected_components:
        cleanup_options.update(_ask_mcp_cleanup_options(env_vars))
    elif env_vars:
        # Even if MCP not selected, ask about env vars if they exist
        cleanup_env = confirm(f"Remove {len(env_vars)} API key environment variables?", default=False)
        cleanup_options['cleanup_env_vars'] = cleanup_env
        if cleanup_env:
            create_script = confirm("Create restore script for environment variables?", default=True)
            cleanup_options['create_restore_script'] = create_script
    
    return selected_components, cleanup_options


def _ask_mcp_cleanup_options(env_vars: Dict[str, str]) -> Dict[str, bool]:
    """Ask for MCP-related cleanup options"""
    print(f"\n{Colors.YELLOW}{Colors.BRIGHT}MCP Cleanup Options{Colors.RESET}")
    print("Since you're removing the MCP component:")
    
    cleanup_options = {}
    
    # Ask about MCP server configurations
    remove_configs = confirm("Remove MCP server configurations from .gemini.json?", default=True)
    cleanup_options['remove_mcp_configs'] = remove_configs
    
    # Ask about API key environment variables
    if env_vars:
        print(f"\n{Colors.BLUE}Related API key environment variables found:{Colors.RESET}")
        for env_var, value in env_vars.items():
            masked_value = f"{value[:4]}...{value[-4:]}" if len(value) > 8 else "***"
            print(f"  {env_var}: {masked_value}")
        
        cleanup_env = confirm(f"Remove {len(env_vars)} API key environment variables?", default=False)
        cleanup_options['cleanup_env_vars'] = cleanup_env
        
        if cleanup_env:
            create_script = confirm("Create restore script for environment variables?", default=True)
            cleanup_options['create_restore_script'] = create_script
        else:
            cleanup_options['create_restore_script'] = True
    else:
        cleanup_options['cleanup_env_vars'] = False
        cleanup_options['create_restore_script'] = True
    
    return cleanup_options


def interactive_uninstall_selection(installed_components: Dict[str, str]) -> Optional[List[str]]:
    """Legacy function - redirects to enhanced selection"""
    env_vars = get_supergemini_environment_variables()
    result = interactive_component_selection(installed_components, env_vars)
    
    if result is None:
        return None
    
    # For backwards compatibility, return only component list
    components, cleanup_options = result
    return components


def display_preservation_info() -> None:
    """Show what will NOT be removed (user's custom files)"""
    print(f"\n{Colors.GREEN}{Colors.BRIGHT}Files that will be preserved:{Colors.RESET}")
    print(f"{Colors.GREEN}✓ User's custom commands (not in commands/sg/){Colors.RESET}")
    print(f"{Colors.GREEN}✓ User's custom agents (not SuperGemini agents){Colors.RESET}")
    print(f"{Colors.GREEN}✓ User's custom .gemini.json configurations{Colors.RESET}")
    print(f"{Colors.GREEN}✓ User's custom files in shared directories{Colors.RESET}")
    print(f"{Colors.GREEN}✓ Gemini CLI settings and other tools' configurations{Colors.RESET}")


def display_component_details(component: str, info: Dict[str, Any]) -> Dict[str, Any]:
    """Get detailed information about what will be removed for a component"""
    details = {
        'files': [],
        'directories': [],
        'size': 0,
        'description': ''
    }
    
    install_dir = info['install_dir']
    
    component_paths = {
        'core': {
            'files': ['GEMINI.md', 'FLAGS.md', 'PRINCIPLES.md', 'RULES.md', 'ORCHESTRATOR.md', 'SESSION_LIFECYCLE.md'],
            'description': 'Core framework files in ~/.gemini/'
        },
        'commands': {
            'files': 'commands/sg/*.md',
            'description': 'SuperGemini commands in ~/.gemini/commands/sg/'
        },
        'mcp': {
            'files': 'MCP server configurations in .gemini.json',
            'description': 'MCP server configurations'
        },
        'mcp_docs': {
            'files': 'MCP/*.md',
            'description': 'MCP documentation files'
        },
        'modes': {
            'files': 'MODE_*.md',
            'description': 'SuperGemini operational modes'
        }
    }
    
    if component in component_paths:
        details['description'] = component_paths[component]['description']
        
        # Get actual file count from enhanced detection
        supergemini_files = info.get("supergemini_files", [])
        component_file_count = len([f for f in supergemini_files if component in str(f)])
        details['file_count'] = component_file_count
    
    return details


def display_uninstall_plan(components: List[str], args: argparse.Namespace, info: Dict[str, Any], env_vars: Dict[str, str]) -> None:
    """Display detailed uninstall plan with enhanced information"""
    print(f"\n{Colors.CYAN}{Colors.BRIGHT}Enhanced Uninstall Plan{Colors.RESET}")
    print("=" * 60)
    
    print(f"{Colors.BLUE}Installation Directory:{Colors.RESET} {info['install_dir']}")
    
    # Show file analysis
    supergemini_count = len(info.get("supergemini_files", []))
    preserved_count = len(info.get("preserved_files", []))
    
    print(f"\n{Colors.BLUE}File Analysis:{Colors.RESET}")
    print(f"{Colors.RED}SuperGemini files to remove: {supergemini_count}{Colors.RESET}")
    print(f"{Colors.GREEN}User files to preserve: {preserved_count}{Colors.RESET}")
    
    if components:
        print(f"\n{Colors.BLUE}Components to remove:{Colors.RESET}")
        
        for i, component_name in enumerate(components, 1):
            details = display_component_details(component_name, info)
            version = info["components"].get(component_name, "unknown")
            
            if isinstance(version, dict):
                version_str = version.get('version', 'unknown')
            else:
                version_str = str(version)
                
            file_count = details.get('file_count', '?')
            print(f"  {i}. {component_name} (v{version_str}) - {file_count} files")
            print(f"     {details['description']}")
    
    # Show detailed preservation information
    print(f"\n{Colors.GREEN}{Colors.BRIGHT}Enhanced Safety Guarantees - Will Preserve:{Colors.RESET}")
    print(f"{Colors.GREEN}✓ User's custom commands (not in commands/sg/){Colors.RESET}")
    print(f"{Colors.GREEN}✓ User's custom agents (not SuperGemini agents){Colors.RESET}")
    print(f"{Colors.GREEN}✓ User's .gemini.json customizations{Colors.RESET}")
    print(f"{Colors.GREEN}✓ Gemini CLI settings and other tools' configurations{Colors.RESET}")
    print(f"{Colors.GREEN}✓ All non-SuperGemini files (verified by content analysis){Colors.RESET}")
    
    # Show additional preserved items
    preserved = []
    if args.keep_backups:
        preserved.append("backup files")
    if args.keep_logs:
        preserved.append("log files") 
    if args.keep_settings:
        preserved.append("user settings")
    
    if preserved:
        for item in preserved:
            print(f"{Colors.GREEN}✓ {item}{Colors.RESET}")
    
    if args.complete:
        print(f"\n{Colors.RED}⚠️  WARNING: Complete uninstall will remove all {supergemini_count} SuperGemini files{Colors.RESET}")
        print(f"{Colors.GREEN}✓ {preserved_count} user files will be preserved{Colors.RESET}")
    
    # Environment variable cleanup information
    if env_vars:
        print(f"\n{Colors.BLUE}Environment Variables:{Colors.RESET}")
        if args.cleanup_env:
            print(f"{Colors.YELLOW}Will remove {len(env_vars)} API key environment variables:{Colors.RESET}")
            for env_var in env_vars.keys():
                print(f"  - {env_var}")
            if not args.no_restore_script:
                print(f"{Colors.GREEN}  ✓ Restore script will be created{Colors.RESET}")
        else:
            print(f"{Colors.BLUE}Will preserve {len(env_vars)} API key environment variables:{Colors.RESET}")
            for env_var in env_vars.keys():
                print(f"  ✓ {env_var}")
    
    print()


def create_uninstall_backup(install_dir: Path, components: List[str], supergemini_files: List[Path]) -> Optional[Path]:
    """Create comprehensive backup before uninstall"""
    logger = get_logger()
    
    try:
        from datetime import datetime
        backup_dir = install_dir / "backups"
        backup_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"supergemini_backup_{timestamp}.tar.gz"
        backup_path = backup_dir / backup_name
        
        import tarfile
        
        logger.info(f"Creating comprehensive backup: {backup_path}")
        
        with tarfile.open(backup_path, "w:gz") as tar:
            # Backup all SuperGemini files
            for file_path in supergemini_files:
                try:
                    if file_path.exists():
                        arcname = file_path.relative_to(install_dir)
                        tar.add(file_path, arcname=arcname)
                except Exception as e:
                    logger.debug(f"Could not backup {file_path}: {e}")
        
        logger.success(f"Backup created: {backup_path}")
        return backup_path
        
    except Exception as e:
        logger.warning(f"Could not create backup: {e}")
        return None


def perform_enhanced_uninstall(components: List[str], args: argparse.Namespace, info: Dict[str, Any], env_vars: Dict[str, str]) -> bool:
    """Perform the enhanced SuperGemini uninstall with complete file removal"""
    logger = get_logger()
    start_time = time.time()
    
    try:
        # Get SuperGemini files to remove
        supergemini_files = info.get("supergemini_files", [])
        preserved_files = info.get("preserved_files", [])
        
        logger.info(f"Enhanced uninstall: {len(supergemini_files)} SuperGemini files, {len(preserved_files)} preserved files")
        
        # Setup progress tracking
        total_operations = len(supergemini_files) + len(components) + (1 if args.cleanup_env and env_vars else 0)
        progress = ProgressBar(
            total=total_operations,
            prefix="Uninstalling: ",
            suffix=""
        )
        
        file_manager = FileService()
        
        # Phase 1: Remove individual SuperGemini files
        logger.info("Phase 1: Removing SuperGemini files...")
        removed_files = []
        failed_files = []
        
        # Close log handlers first to prevent file lock issues
        import logging
        # Access the internal logging.Logger through the wrapper
        internal_logger = logger.logger if hasattr(logger, 'logger') else logger
        for handler in internal_logger.handlers[:]:
            if hasattr(handler, 'close'):
                handler.close()
            internal_logger.removeHandler(handler)
        
        for i, file_path in enumerate(supergemini_files):
            progress.update(i, f"Removing {file_path.name}")
            
            try:
                if file_path.exists():
                    # Special handling for log files - ensure they're not locked
                    if '.log' in file_path.suffix or 'log' in file_path.name.lower():
                        # Force close any file handles
                        import gc
                        gc.collect()
                        time.sleep(0.1)  # Brief wait for file handles to release
                    
                    if file_manager.remove_file(file_path):
                        removed_files.append(file_path)
                        print(f"✓ Successfully removed: {file_path}")
                    else:
                        failed_files.append(file_path)
                        print(f"✗ Failed to remove: {file_path}")
                else:
                    print(f"- File already removed: {file_path}")
                    
            except Exception as e:
                print(f"Error removing file {file_path}: {e}")
                failed_files.append(file_path)
                
            time.sleep(0.01)  # Brief pause
        
        # Phase 2: Component-specific cleanup
        logger.info("Phase 2: Component cleanup...")
        
        try:
            registry = ComponentRegistry(get_safe_components_directory())
            registry.discover_components()
            
            component_instances = {}
            for component_name in components:
                try:
                    instance = registry.get_component_instance(component_name, args.install_dir)
                    if instance:
                        component_instances[component_name] = instance
                except Exception as e:
                    logger.error(f"Error creating instance for {component_name}: {e}")
        except Exception as e:
            logger.error(f"Error creating component registry: {e}")
            component_instances = {}
        
        uninstalled_components = []
        failed_components = []
        
        for i, component_name in enumerate(components):
            progress.update(len(supergemini_files) + i, f"Cleaning {component_name}")
            
            try:
                if component_name in component_instances:
                    instance = component_instances[component_name]
                    if instance.uninstall():
                        uninstalled_components.append(component_name)
                        logger.debug(f"Successfully cleaned {component_name}")
                    else:
                        failed_components.append(component_name)
                        logger.error(f"Failed to clean {component_name}")
                else:
                    logger.warning(f"Component {component_name} not found, skipping")
                    
            except Exception as e:
                logger.error(f"Error cleaning {component_name}: {e}")
                failed_components.append(component_name)
        
        # Phase 3: Environment variable cleanup
        env_cleanup_success = True
        if args.cleanup_env and env_vars:
            progress.update(len(supergemini_files) + len(components), "Cleaning environment")
            logger.info("Phase 3: Cleaning up environment variables...")
            create_restore_script = not args.no_restore_script
            env_cleanup_success = cleanup_environment_variables(env_vars, create_restore_script)
            
            if env_cleanup_success:
                logger.success(f"Removed {len(env_vars)} environment variables")
            else:
                logger.warning("Some environment variables could not be removed")
        
        # Phase 4: Clean up empty directories
        logger.info("Phase 4: Cleaning empty directories...")
        cleanup_empty_directories(args.install_dir, preserve_patterns=None if args.complete else ['*'])
        
        progress.finish("Enhanced uninstall complete")
        
        # Show comprehensive results
        duration = time.time() - start_time
        
        print(f"\n{Colors.CYAN}{Colors.BRIGHT}Uninstall Results{Colors.RESET}")
        print("=" * 50)
        
        print(f"{Colors.GREEN}Successfully removed:{Colors.RESET}")
        print(f"  SuperGemini files: {len(removed_files)}")
        print(f"  Components: {len(uninstalled_components)}")
        if args.cleanup_env and env_vars and env_cleanup_success:
            print(f"  Environment variables: {len(env_vars)}")
        
        print(f"{Colors.BLUE}Preserved files: {len(preserved_files)}{Colors.RESET}")
        
        if failed_files or failed_components:
            print(f"\n{Colors.YELLOW}Issues encountered:{Colors.RESET}")
            if failed_files:
                print(f"  Failed to remove {len(failed_files)} files")
            if failed_components:
                print(f"  Failed to clean {len(failed_components)} components")
        
        # Final verification
        remaining_files = verify_complete_removal(args.install_dir)
        if remaining_files:
            print(f"\n{Colors.YELLOW}Note: {len(remaining_files)} SuperGemini files may still remain{Colors.RESET}")
            logger.warning(f"Incomplete removal: {len(remaining_files)} files remain")
            return False
        else:
            print(f"\n{Colors.GREEN}✓ Complete removal verified - no SuperGemini files remain{Colors.RESET}")
            logger.success(f"Complete uninstall verified in {duration:.1f} seconds")
            return True
        
    except Exception as e:
        logger.exception(f"Unexpected error during enhanced uninstall: {e}")
        return False


def cleanup_empty_directories(install_dir: Path, preserve_patterns: Optional[List[str]] = None) -> None:
    """Clean up empty directories after file removal"""
    logger = get_logger()
    
    try:
        # Find all directories
        all_dirs = []
        for item in install_dir.rglob("*"):
            if item.is_dir():
                all_dirs.append(item)
        
        # Sort by depth (deepest first) to remove from bottom up
        all_dirs.sort(key=lambda p: len(p.parts), reverse=True)
        
        file_manager = FileService()
        
        for directory in all_dirs:
            try:
                # Skip if it's the install directory itself
                if directory == install_dir:
                    continue
                
                # Check if directory is empty
                if directory.exists() and not any(directory.iterdir()):
                    logger.debug(f"Removing empty directory: {directory}")
                    file_manager.remove_directory(directory)
                    
            except Exception as e:
                logger.debug(f"Could not remove directory {directory}: {e}")
                
    except Exception as e:
        logger.debug(f"Error during directory cleanup: {e}")


def verify_complete_removal(install_dir: Path) -> List[Path]:
    """Verify that all SuperGemini files have been removed"""
    if not install_dir.exists():
        return []
    
    try:
        detector = SuperGeminiFileDetector(install_dir)
        supergemini_files, _ = detector.scan_all_files()
        return supergemini_files
    except Exception:
        return []


def perform_uninstall(components: List[str], args: argparse.Namespace, info: Dict[str, Any], env_vars: Dict[str, str]) -> bool:
    """Legacy wrapper for enhanced uninstall"""
    return perform_enhanced_uninstall(components, args, info, env_vars)


def cleanup_installation_directory(install_dir: Path, args: argparse.Namespace) -> None:
    """Enhanced installation directory cleanup"""
    logger = get_logger()
    file_manager = FileService()
    
    try:
        # Use enhanced detector to identify SuperGemini files
        detector = SuperGeminiFileDetector(install_dir)
        supergemini_files, preserved_files = detector.scan_all_files()
        
        # Build preserve patterns
        preserve_patterns = []
        
        if args.keep_backups:
            preserve_patterns.extend(["backups/*", "*.backup", "*.bak"])
        if args.keep_logs:
            preserve_patterns.extend(["logs/*", "*.log"])
        if args.keep_settings:
            preserve_patterns.extend(["settings.json", ".gemini.json", "config/*"])
        
        # Remove SuperGemini files specifically
        logger.info(f"Removing {len(supergemini_files)} SuperGemini files...")
        for file_path in supergemini_files:
            try:
                if file_path.exists():
                    file_manager.remove_file(file_path)
            except Exception as e:
                logger.debug(f"Could not remove {file_path}: {e}")
        
        # Clean up empty directories
        cleanup_empty_directories(install_dir, preserve_patterns)
        
        logger.info(f"Cleanup complete: removed SuperGemini files, preserved {len(preserved_files)} user files")
        
    except Exception as e:
        logger.error(f"Error during enhanced cleanup: {e}")


def run(args: argparse.Namespace) -> int:
    """Execute enhanced uninstall operation with comprehensive file detection"""
    operation = UninstallOperation()
    operation.setup_operation_logging(args)
    logger = get_logger()
    
    # Security validation
    expected_home = Path.home().resolve()
    actual_dir = args.install_dir.resolve()

    if not str(actual_dir).startswith(str(expected_home)):
        print(f"\n[✗] Installation must be inside your user profile directory.")
        print(f"    Expected prefix: {expected_home}")
        print(f"    Provided path:   {actual_dir}")
        sys.exit(1)
    
    try:
        # Validate global arguments
        success, errors = operation.validate_global_args(args)
        if not success:
            for error in errors:
                logger.error(error)
            return 1
        
        # Display header
        if not args.quiet:
            from setup import __version__
            display_header(
                f"SuperGemini Enhanced Uninstall v{__version__}",
                "Complete SuperGemini framework removal with advanced file detection"
            )
        
        # Get enhanced installation information
        try:
            info = get_installation_info(args.install_dir)
            logger.info(f"Enhanced analysis: found {len(info.get('supergemini_files', []))} SuperGemini files, {len(info.get('preserved_files', []))} user files")
        except RecursionError:
            logger.error("Recursion detected in get_installation_info. Using basic cleanup.")
            # Fallback to basic cleanup
            if args.install_dir.exists():
                if not args.no_confirm:
                    if confirm(f"Remove SuperGemini directory {args.install_dir}?", default=False):
                        import shutil
                        shutil.rmtree(args.install_dir)
                        logger.success("SuperGemini directory removed")
                        return 0
            return 1
        
        # Display enhanced installation information
        if not args.quiet:
            try:
                display_uninstall_info(info)
            except RecursionError:
                logger.error("Recursion detected in display_uninstall_info")
                print(f"Installation Directory: {info['install_dir']}")
                print(f"SuperGemini files: {len(info.get('supergemini_files', []))}")
                print(f"Preserved files: {len(info.get('preserved_files', []))}")
        
        # Check environment variables
        try:
            env_vars = display_environment_info() if not args.quiet else get_supergemini_environment_variables()
        except RecursionError:
            logger.error("Recursion detected in environment variable functions")
            env_vars = {}
        
        # Check if SuperGemini is installed
        if not info["exists"]:
            logger.warning(f"No SuperGemini installation found in {args.install_dir}")
            return 0
        
        # Check if any SuperGemini files exist
        supergemini_files = info.get("supergemini_files", [])
        if not supergemini_files and not info["components"]:
            logger.info(f"No SuperGemini files or components found in {args.install_dir}")
            
            # Offer to clean up empty directory
            if info["exists"] and (info["files"] or info["directories"]):
                if not args.no_confirm:
                    if confirm(f"Remove empty directory {args.install_dir}?", default=False):
                        try:
                            import shutil
                            shutil.rmtree(args.install_dir)
                            logger.success(f"Removed directory {args.install_dir}")
                        except Exception as e:
                            logger.error(f"Could not remove directory: {e}")
            return 0
        
        # Get components to uninstall using enhanced selection
        if args.components or args.complete:
            # Non-interactive mode
            components = get_components_to_uninstall(args, info["components"])
            cleanup_options = {
                'remove_mcp_configs': 'mcp' in (components or []),
                'cleanup_env_vars': args.cleanup_env,
                'create_restore_script': not args.no_restore_script
            }
            if components is None:
                logger.info("Uninstall cancelled by user")
                return 0
            elif not components:
                # Even if no components, remove SuperGemini files
                components = []
        else:
            # Interactive mode
            result = interactive_component_selection(info["components"], env_vars)
            if result is None:
                logger.info("Uninstall cancelled by user")
                return 0
            elif not result:
                logger.info("No components selected for uninstall")
                # Still proceed to remove any SuperGemini files found
                components = []
                cleanup_options = {
                    'remove_mcp_configs': False,
                    'cleanup_env_vars': False,
                    'create_restore_script': True
                }
            else:
                components, cleanup_options = result
                # Override command-line args with interactive choices
                args.cleanup_env = cleanup_options.get('cleanup_env_vars', False)
                args.no_restore_script = not cleanup_options.get('create_restore_script', True)
        
        # Display enhanced uninstall plan
        if not args.quiet:
            display_uninstall_plan(components, args, info, env_vars)
        
        # Enhanced confirmation
        if not args.no_confirm and not args.yes:
            supergemini_count = len(info.get("supergemini_files", []))
            if args.complete or supergemini_count > 0:
                if args.complete:
                    warning_msg = f"This will completely remove {supergemini_count} SuperGemini files. Continue?"
                else:
                    warning_msg = f"This will remove {supergemini_count} SuperGemini files and {len(components)} component(s). Continue?"
                
                if not confirm(warning_msg, default=False):
                    logger.info("Uninstall cancelled by user")
                    return 0
        
        # Create comprehensive backup
        if not args.dry_run and not args.keep_backups and supergemini_files:
            create_uninstall_backup(args.install_dir, components, supergemini_files)
        
        # Perform enhanced uninstall
        success = perform_enhanced_uninstall(components, args, info, env_vars)
        
        if success:
            if not args.quiet:
                display_success("SuperGemini enhanced uninstall completed successfully!")
                
                if not args.dry_run:
                    print(f"\n{Colors.CYAN}Enhanced Uninstall Complete:{Colors.RESET}")
                    print(f"SuperGemini has been completely removed from {args.install_dir}")
                    print(f"All user files have been preserved")
                    if not args.complete:
                        print(f"You can reinstall anytime using 'SuperGemini install'")
                    
            return 0
        else:
            display_error("Uninstall completed with some issues. Check logs for details.")
            return 1
            
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Uninstall cancelled by user{Colors.RESET}")
        return 130
    except Exception as e:
        return operation.handle_operation_error("uninstall", e)