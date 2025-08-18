"""
Safe path utilities for SuperGemini component discovery
Handles PyPI installation, development, and various deployment scenarios
"""

from pathlib import Path
from typing import Optional
import os

def get_safe_components_directory() -> Optional[Path]:
    """
    Get components directory with fallback strategies for different installation scenarios
    
    Returns:
        Path to components directory or None if not found
    """
    
    # Strategy 1: Development/editable install
    # This file is at setup/utils/paths.py, so components should be at setup/components
    current_file = Path(__file__)
    setup_dir = current_file.parent.parent  # setup/
    dev_components_dir = setup_dir / "components"
    
    if dev_components_dir.exists() and dev_components_dir.is_dir():
        # Verify it contains component files
        component_files = list(dev_components_dir.glob("*.py"))
        if component_files and any(f.name != "__init__.py" for f in component_files):
            return dev_components_dir
    
    # Strategy 2: PyPI wheel install
    # In wheel packages, components might be at different relative location
    package_root = current_file.parent.parent.parent  # Go up to package root
    wheel_components_dir = package_root / "setup" / "components"
    
    if wheel_components_dir.exists() and wheel_components_dir.is_dir():
        component_files = list(wheel_components_dir.glob("*.py"))
        if component_files and any(f.name != "__init__.py" for f in component_files):
            return wheel_components_dir
    
    # Strategy 3: Site-packages install with different structure
    # Look for components relative to current module location
    try:
        import setup
        setup_module_path = Path(setup.__file__).parent
        site_components_dir = setup_module_path / "components"
        
        if site_components_dir.exists() and site_components_dir.is_dir():
            component_files = list(site_components_dir.glob("*.py"))
            if component_files and any(f.name != "__init__.py" for f in component_files):
                return site_components_dir
    except (ImportError, AttributeError):
        pass
    
    # Strategy 4: Environment variable override
    # Allow explicit override for custom installations
    env_components_path = os.getenv("SUPERGEMINI_COMPONENTS_PATH")
    if env_components_path:
        env_components_dir = Path(env_components_path)
        if env_components_dir.exists() and env_components_dir.is_dir():
            return env_components_dir
    
    # Strategy 5: Search in common locations
    # Last resort - search in possible locations
    common_locations = [
        current_file.parent.parent / "components",
        current_file.parent.parent.parent / "setup" / "components",
        Path.cwd() / "setup" / "components",
    ]
    
    for location in common_locations:
        if location.exists() and location.is_dir():
            component_files = list(location.glob("*.py"))
            if component_files and any(f.name != "__init__.py" for f in component_files):
                return location
    
    return None

def validate_components_directory(components_dir: Path) -> bool:
    """
    Validate that components directory contains valid component files
    
    Args:
        components_dir: Path to components directory
        
    Returns:
        True if directory contains valid components
    """
    if not components_dir.exists() or not components_dir.is_dir():
        return False
    
    # Check for Python files
    python_files = list(components_dir.glob("*.py"))
    if not python_files:
        return False
    
    # Must have files other than __init__.py
    component_files = [f for f in python_files if f.name != "__init__.py"]
    if not component_files:
        return False
    
    # Check for expected component files
    expected_components = ["core.py", "mcp.py", "agents.py", "commands.py", "modes.py"]
    found_components = [f.name for f in component_files]
    
    # At least core.py should exist
    if "core.py" not in found_components:
        return False
    
    return True

def get_project_root() -> Optional[Path]:
    """
    Get project root directory with fallback strategies
    
    Returns:
        Path to project root or None if not found
    """
    components_dir = get_safe_components_directory()
    if components_dir:
        # Components dir is at setup/components, so project root is two levels up
        return components_dir.parent.parent
    
    return None