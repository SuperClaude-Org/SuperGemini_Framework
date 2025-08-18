#!/usr/bin/env python3
"""
Version update utility for SuperGemini Framework
Updates all hardcoded version strings to match VERSION file (SSOT)
"""

import re
from pathlib import Path

def get_version():
    """Read version from VERSION file"""
    version_file = Path(__file__).parent / "VERSION"
    if version_file.exists():
        return version_file.read_text().strip()
    else:
        raise FileNotFoundError("VERSION file not found")

def update_file_versions(file_path: Path, old_version: str, new_version: str):
    """Update version strings in a single file"""
    content = file_path.read_text()
    
    # Pattern to match version strings (e.g., 4.0.3, 4.0.4)
    pattern = re.compile(r'\b\d+\.\d+\.\d+\b')
    
    # Replace all version-like strings that match the old version pattern
    updated = False
    new_content = content
    
    for match in pattern.finditer(content):
        version_str = match.group()
        if version_str.startswith('4.0.'):  # Only update SuperGemini versions
            new_content = new_content.replace(version_str, new_version)
            updated = True
    
    if updated:
        file_path.write_text(new_content)
        print(f"Updated {file_path}")
        return True
    return False

def main():
    """Main function to update all version strings"""
    # Get current version from VERSION file
    new_version = get_version()
    print(f"Updating all files to version {new_version}")
    
    # Define directories to search
    project_root = Path(__file__).parent
    dirs_to_search = [
        project_root / "setup",
        project_root / "SuperGemini",
    ]
    
    # Find and update Python files
    updated_count = 0
    for directory in dirs_to_search:
        if directory.exists():
            for py_file in directory.rglob("*.py"):
                if update_file_versions(py_file, "4.0.3", new_version):
                    updated_count += 1
    
    print(f"\nUpdated {updated_count} files to version {new_version}")
    print("Note: This is a temporary solution. Files should be refactored to use dynamic version loading.")

if __name__ == "__main__":
    main()