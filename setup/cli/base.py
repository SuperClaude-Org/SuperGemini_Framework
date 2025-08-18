"""
SuperGemini Operations Module

This module contains all SuperGemini management operations that can be
executed through the unified CLI hub (SuperGemini).

Each operation module should implement:
- register_parser(subparsers): Register CLI arguments for the operation
- run(args): Execute the operation with parsed arguments

Available operations:
- install: Install SuperGemini framework components
- update: Update existing SuperGemini installation
- uninstall: Remove SuperGemini framework installation  
- backup: Backup and restore SuperGemini installations
"""

# Import version from SSOT
try:
    from setup import __version__
except ImportError:
    # Fallback if main setup module is not available
    from pathlib import Path
    try:
        version_file = Path(__file__).parent.parent.parent / "VERSION"
        if version_file.exists():
            __version__ = version_file.read_text().strip()
        else:
            __version__ = "4.0.4"  # Fallback
    except Exception:
        __version__ = "4.0.4"  # Final fallback
__all__ = ["install", "update", "uninstall", "backup"]


def get_operation_info():
    """Get information about available operations"""
    return {
        "install": {
            "name": "install",
            "description": "Install SuperGemini framework components",
            "module": "setup.operations.install"
        },
        "update": {
            "name": "update", 
            "description": "Update existing SuperGemini installation",
            "module": "setup.operations.update"
        },
        "uninstall": {
            "name": "uninstall",
            "description": "Remove SuperGemini framework installation", 
            "module": "setup.operations.uninstall"
        },
        "backup": {
            "name": "backup",
            "description": "Backup and restore SuperGemini installations",
            "module": "setup.operations.backup"
        }
    }


class OperationBase:
    """Base class for all operations providing common functionality"""
    
    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.logger = None
    
    def setup_operation_logging(self, args):
        """Setup operation-specific logging"""
        from ..utils.logger import get_logger
        self.logger = get_logger()
        self.logger.info(f"Starting {self.operation_name} operation")
    
    def validate_global_args(self, args):
        """Validate global arguments common to all operations"""
        errors = []
        
        # Validate install directory
        if hasattr(args, 'install_dir') and args.install_dir:
            from ..utils.security import SecurityValidator
            is_safe, validation_errors = SecurityValidator.validate_installation_target(args.install_dir)
            if not is_safe:
                errors.extend(validation_errors)
        
        # Check for conflicting flags
        if hasattr(args, 'verbose') and hasattr(args, 'quiet'):
            if args.verbose and args.quiet:
                errors.append("Cannot specify both --verbose and --quiet")
        
        return len(errors) == 0, errors
    
    def handle_operation_error(self, operation: str, error: Exception):
        """Standard error handling for operations"""
        try:
            error_msg = str(error)
        except:
            error_msg = repr(error)
        
        if self.logger:
            self.logger.error(f"Error in {operation} operation: {error_msg}")
            if hasattr(error, '__traceback__'):
                import traceback
                self.logger.debug(traceback.format_exc())
        else:
            print(f"Error in {operation} operation: {error_msg}")
        return 1