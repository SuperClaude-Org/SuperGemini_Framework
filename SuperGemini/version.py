"""
Version management module for SuperGemini Framework
Single Source of Truth (SSOT) for version information
"""

from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def get_version() -> str:
    """
    Get the version from VERSION file (Single Source of Truth).
    
    Returns:
        str: Version string from VERSION file, or fallback if not found
    """
    # Try multiple paths to find VERSION file
    possible_paths = [
        Path(__file__).parent.parent / "VERSION",  # From installed package
        Path.cwd() / "VERSION",  # From current directory
        Path(__file__).parent / "VERSION",  # From package directory
    ]
    
    for version_path in possible_paths:
        if version_path.exists():
            try:
                version = version_path.read_text().strip()
                if version:
                    return version
            except Exception as e:
                logger.warning(f"Failed to read VERSION file at {version_path}: {e}")
                continue
    
    # Fallback version - should only be used if VERSION file is completely missing
    logger.warning("VERSION file not found in any expected location, using fallback")
    return "4.0.4"

# Export the version as a module constant
__version__ = get_version()