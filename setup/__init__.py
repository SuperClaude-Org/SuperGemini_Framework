"""
SuperGemini Installation Suite
Pure Python installation system for SuperGemini framework
"""

__version__ = "3.0.0"
__author__ = "SuperGemini Team"

from pathlib import Path

# Core paths
SETUP_DIR = Path(__file__).parent
PROJECT_ROOT = SETUP_DIR.parent
DATA_DIR = SETUP_DIR / "data"

# Installation target
DEFAULT_INSTALL_DIR = Path.home() / ".claude"