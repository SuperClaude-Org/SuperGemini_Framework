#!/usr/bin/env python
"""
SuperGemini Framework Management Hub
Unified entry point for all SuperGemini operations

Usage:
    SuperGemini install [options]
    SuperGemini update [options]
    SuperGemini uninstall [options]
    SuperGemini backup [options]
    SuperGemini --help
"""

import sys
import argparse
import subprocess
import difflib
from pathlib import Path
from typing import Dict, Callable

# Add the 'setup' directory to the Python import path
# Fix for installed package to find setup module correctly
import os

# First, try to find setup in the installed package location
package_dir = Path(__file__).parent.parent  # SuperGemini package directory

# Check if we're running from installed package or development
if (package_dir / "setup").exists():
    setup_dir = package_dir
else:
    # Fallback to site-packages location
    import site
    for site_dir in site.getsitepackages():
        potential_setup = Path(site_dir) / "setup"
        if potential_setup.exists():
            setup_dir = Path(site_dir)
            break
    else:
        # Last resort: assume setup is in the same directory as SuperGemini
        setup_dir = package_dir

# Add to sys.path
sys.path.insert(0, str(setup_dir))


# Try to import utilities from the setup package
try:
    from setup.utils.ui import (
        display_header, display_info, display_success, display_error,
        display_warning, Colors
    )
    from setup.utils.logger import setup_logging, get_logger, LogLevel
    from setup import DEFAULT_INSTALL_DIR
except ImportError:
    # Provide minimal fallback functions and constants if imports fail
    from pathlib import Path
    DEFAULT_INSTALL_DIR = Path.home() / ".gemini"
    
    class Colors:
        RED = YELLOW = GREEN = CYAN = RESET = BRIGHT = ""

    def display_error(msg): print(f"[ERROR] {msg}")
    def display_warning(msg): print(f"[WARN] {msg}")
    def display_success(msg): print(f"[OK] {msg}")
    def display_info(msg): print(f"[INFO] {msg}")
    def display_header(title, subtitle): print(f"{title} - {subtitle}")
    def get_logger(): return None
    def setup_logging(*args, **kwargs): pass
    class LogLevel:
        ERROR = 40
        INFO = 20
        DEBUG = 10


def create_global_parser() -> argparse.ArgumentParser:
    """Create shared parser for global flags used by all commands"""
    global_parser = argparse.ArgumentParser(add_help=False)

    global_parser.add_argument("--verbose", "-v", action="store_true",
                               help="Enable verbose logging")
    global_parser.add_argument("--quiet", "-q", action="store_true",
                               help="Suppress all output except errors")
    global_parser.add_argument("--install-dir", type=Path, default=DEFAULT_INSTALL_DIR,
                               help=f"Target installation directory (default: {DEFAULT_INSTALL_DIR})")
    global_parser.add_argument("--dry-run", action="store_true",
                               help="Simulate operation without making changes")
    global_parser.add_argument("--force", action="store_true",
                               help="Force execution, skipping checks")
    global_parser.add_argument("--yes", "-y", action="store_true",
                               help="Automatically answer yes to all prompts")

    return global_parser


def create_parser():
    """Create the main CLI parser and attach subcommand parsers"""
    global_parser = create_global_parser()

    parser = argparse.ArgumentParser(
        prog="SuperGemini",
        description="SuperGemini Framework Management Hub - Unified CLI",
        epilog="""
Examples:
  SuperGemini install --dry-run
  SuperGemini update --verbose
  SuperGemini backup --create
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[global_parser]
    )

    parser.add_argument("--version", action="store_true", help="Show version and exit")

    subparsers = parser.add_subparsers(
        dest="operation",
        title="Operations",
        description="Framework operations to perform"
    )

    return parser, subparsers, global_parser


def setup_global_environment(args: argparse.Namespace):
    """Set up logging and shared runtime environment based on args"""
    # Determine log level
    if args.quiet:
        level = LogLevel.ERROR
    elif args.verbose:
        level = LogLevel.DEBUG
    else:
        level = LogLevel.INFO

    # Define log directory unless it's a dry run
    log_dir = args.install_dir / "logs" if not args.dry_run else None
    setup_logging("supergemini_hub", log_dir=log_dir, console_level=level)

    # Log startup context
    logger = get_logger()
    if logger:
        logger.debug(f"SuperGemini called with operation: {getattr(args, 'operation', 'None')}")
        logger.debug(f"Arguments: {vars(args)}")


def get_operation_modules() -> Dict[str, str]:
    """Return supported operations and their descriptions"""
    return {
        "install": "Install SuperGemini framework components",
        "update": "Update existing SuperGemini installation",
        "uninstall": "Remove SuperGemini installation",
        "backup": "Backup and restore operations"
    }


def load_operation_module(name: str):
    """Try to dynamically import an operation module"""
    try:
        return __import__(f"setup.operations.{name}", fromlist=[name])
    except ImportError as e:
        logger = get_logger()
        if logger:
            logger.error(f"Module '{name}' failed to load: {e}")
        return None


def register_operation_parsers(subparsers, global_parser) -> Dict[str, Callable]:
    """Register subcommand parsers and map operation names to their run functions"""
    operations = {}
    for name, desc in get_operation_modules().items():
        module = load_operation_module(name)
        if module and hasattr(module, 'register_parser') and hasattr(module, 'run'):
            module.register_parser(subparsers, global_parser)
            operations[name] = module.run
        else:
            # If module doesn't exist, register a stub parser and fallback to legacy
            parser = subparsers.add_parser(name, help=f"{desc} (legacy fallback)", parents=[global_parser])
            parser.add_argument("--legacy", action="store_true", help="Use legacy script")
            operations[name] = None
    return operations


def handle_legacy_fallback(op: str, args: argparse.Namespace) -> int:
    """Run a legacy operation script if module is unavailable"""
    script_path = Path(__file__).parent / f"{op}.py"

    if not script_path.exists():
        display_error(f"No module or legacy script found for operation '{op}'")
        return 1

    display_warning(f"Falling back to legacy script for '{op}'...")

    cmd = [sys.executable, str(script_path)]

    # Convert args into CLI flags
    for k, v in vars(args).items():
        if k in ['operation', 'install_dir'] or v in [None, False]:
            continue
        flag = f"--{k.replace('_', '-')}"
        if v is True:
            cmd.append(flag)
        else:
            cmd.extend([flag, str(v)])

    try:
        return subprocess.call(cmd)
    except Exception as e:
        display_error(f"Legacy execution failed: {e}")
        return 1


def main() -> int:
    """Main entry point"""
    try:
        parser, subparsers, global_parser = create_parser()
        operations = register_operation_parsers(subparsers, global_parser)
        args = parser.parse_args()

        # Handle --version flag
        if hasattr(args, 'version') and args.version:
            print("SuperGemini v3.2.2")
            return 0

        # No operation provided? Show help manually unless in quiet mode
        if not hasattr(args, 'operation') or not args.operation:
            if not args.quiet:
                display_header("SuperGemini Framework v3.2.2", "Unified CLI for all operations")
                print(f"{Colors.CYAN}Available operations:{Colors.RESET}")
                for op, desc in get_operation_modules().items():
                    print(f"  {op:<12} {desc}")
            return 0

        # Handle unknown operations and suggest corrections
        if args.operation not in operations:
            close = difflib.get_close_matches(args.operation, operations.keys(), n=1)
            suggestion = f"Did you mean: {close[0]}?" if close else ""
            display_error(f"Unknown operation: '{args.operation}'. {suggestion}")
            return 1

        # Setup global context (logging, install path, etc.)
        setup_global_environment(args)
        logger = get_logger()

        # Execute operation
        run_func = operations.get(args.operation)
        if run_func:
            if logger:
                logger.info(f"Executing operation: {args.operation}")
            return run_func(args)
        else:
            # Fallback to legacy script
            if logger:
                logger.warning(f"Module for '{args.operation}' missing, using legacy fallback")
            return handle_legacy_fallback(args.operation, args)

    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Operation cancelled by user{Colors.RESET}")
        return 130
    except Exception as e:
        try:
            logger = get_logger()
            if logger:
                logger.exception(f"Unhandled error: {e}")
        except:
            print(f"{Colors.RED}[ERROR] {e}{Colors.RESET}")
        return 1


# Entrypoint guard
if __name__ == "__main__":
    sys.exit(main())
    

