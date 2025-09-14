"""
Version management module for SuperGemini Framework
Single Source of Truth (SSOT) for version information
"""

def get_version() -> str:
    """
    Get the version from VERSION file (Single Source of Truth).
    Simplified version that minimizes logging and file system access.
    """
    from pathlib import Path
    
    # Try the most common locations in order of likelihood
    version_locations = [
        # Package-local VERSION (for wheel installs)
        Path(__file__).parent / "VERSION",
        # Project root VERSION (for editable installs)  
        Path(__file__).parent.parent / "VERSION",
    ]
    
    for location in version_locations:
        try:
            if location.exists():
                return location.read_text().strip()
        except:
            continue
    
    # Fallback version - no logging needed since this is expected behavior
    return "4.0.9"

__version__ = get_version()
