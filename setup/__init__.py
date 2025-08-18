"""
SuperGemini Installation Suite
Pure Python installation system for SuperGemini framework
"""

from pathlib import Path

# SSOT: Read version from VERSION file
def _get_version():
    """Get version from VERSION file (Single Source of Truth)"""
    try:
        version_file = Path(__file__).parent.parent / "VERSION"
        if version_file.exists():
            return version_file.read_text().strip()
    except Exception:
        pass
    return "4.0.4"  # Fallback only if VERSION file is missing

__version__ = _get_version()

__author__ = "SuperGemini-Org"

# Core paths
SETUP_DIR = Path(__file__).parent
PROJECT_ROOT = SETUP_DIR.parent
DATA_DIR = SETUP_DIR / "data"

# Installation target
DEFAULT_INSTALL_DIR = Path.home() / ".gemini"