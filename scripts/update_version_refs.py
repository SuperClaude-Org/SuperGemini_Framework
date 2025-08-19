#!/usr/bin/env python3
"""
Update version references in README.md and package.json from VERSION file
Single Source of Truth (SSOT) version management
"""

import json
import re
from pathlib import Path

def get_version():
    """Read version from VERSION file"""
    version_file = Path(__file__).parent.parent / "VERSION"
    if version_file.exists():
        return version_file.read_text().strip()
    return "4.0.5"

def update_readme_version(version):
    """Update version badge in README.md"""
    readme_path = Path(__file__).parent.parent / "README.md"
    content = readme_path.read_text()
    
    # Update version badge
    pattern = r'(https://img\.shields\.io/badge/version-)[^-]+(-.*.svg)'
    replacement = f'\\g<1>{version}\\g<2>'
    content = re.sub(pattern, replacement, content)
    
    readme_path.write_text(content)
    print(f"✅ Updated README.md version badge to {version}")

def update_package_json_version(version):
    """Update version in package.json"""
    package_path = Path(__file__).parent.parent / "package.json"
    
    with open(package_path, 'r') as f:
        data = json.load(f)
    
    data['version'] = version
    
    with open(package_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Updated package.json version to {version}")

def main():
    version = get_version()
    print(f"📦 Current VERSION file: {version}")
    
    update_readme_version(version)
    update_package_json_version(version)
    
    print(f"🎉 All version references updated to {version}")

if __name__ == "__main__":
    main()