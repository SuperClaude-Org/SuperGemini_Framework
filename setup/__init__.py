"""
SuperGemini Installation Suite
Pure Python installation system for SuperGemini framework
"""

__version__ = "3.2.2"
__author__ = "SuperGemini Team"

from pathlib import Path

# Core paths
SETUP_DIR = Path(__file__).parent
PROJECT_ROOT = SETUP_DIR.parent
CONFIG_DIR = PROJECT_ROOT / "config"
PROFILES_DIR = PROJECT_ROOT / "profiles"

# Installation target
DEFAULT_INSTALL_DIR = Path.home() / ".gemini"