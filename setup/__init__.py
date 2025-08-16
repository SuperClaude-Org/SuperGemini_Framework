"""
SuperClaude Installation Suite
Pure Python installation system for SuperClaude framework
"""

__version__ = "4.0.0b1"
__author__ = "hyunjae-labs"

from pathlib import Path

# Core paths
SETUP_DIR = Path(__file__).parent
PROJECT_ROOT = SETUP_DIR.parent
DATA_DIR = SETUP_DIR / "data"

# Installation target
DEFAULT_INSTALL_DIR = Path.home() / ".gemini"