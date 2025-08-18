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
    """
    # Base project root (two levels up from this file: pd/SuperGemini/version.py → pd/)
    project_root = Path(__file__).resolve().parent.parent

    possible_paths = [
        project_root / "VERSION",        # Correct: pd/VERSION
        Path.cwd() / "VERSION",          # Current working directory
        Path(__file__).resolve().parent / "VERSION",  # Local fallback
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

    # Fallback
    logger.warning("VERSION file not found in any expected location, using fallback")
    return "4.0.5"

__version__ = get_version()
