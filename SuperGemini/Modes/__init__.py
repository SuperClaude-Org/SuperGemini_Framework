#!/usr/bin/env python3
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

# Import version from SSOT
try:
    from ..version import __version__
except ImportError:
    # Fallback if version module is not available
    from pathlib import Path
    try:
        version_file = Path(__file__).parent.parent.parent / "VERSION"
        if version_file.exists():
            __version__ = version_file.read_text().strip()
        else:
            __version__ = "4.0.7"  # Fallback
    except Exception:
        __version__ = "4.0.7"  # Final fallback
__author__ = "NomenAK, Mithun Gowda B"
__email__ = "anton.knoery@gmail.com"
__license__ = "MIT"
