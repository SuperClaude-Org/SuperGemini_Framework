#!/usr/bin/env python3
"""
Script to clean up personal information from SuperGemini codebase
Run this to replace personal emails with organizational emails
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

def find_and_replace_in_file(file_path: Path, replacements: List[Tuple[str, str]]) -> bool:
    """Replace patterns in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main cleanup function"""
    
    # Define replacements
    replacements = [
        (r'thecurrent\.lim@gmail\.com', 'support@supergemini.org'),
        (r'hyunjae-labs', 'SuperGemini-Team'),
        # Keep the actual name in author fields but change email
    ]
    
    # Files to update
    files_to_update = [
        'pyproject.toml',
        'setup.py',
        'SECURITY.md',
    ]
    
    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    print("SuperGemini Personal Information Cleanup")
    print("=" * 50)
    
    # Process each file
    for file_name in files_to_update:
        file_path = project_root / file_name
        if file_path.exists():
            print(f"Processing: {file_name}")
            if find_and_replace_in_file(file_path, replacements):
                print(f"  ✅ Updated {file_name}")
            else:
                print(f"  ⏭️  No changes needed in {file_name}")
        else:
            print(f"  ⚠️  File not found: {file_name}")
    
    # Check for api-key.txt
    api_key_file = project_root.parent.parent / '05-resources' / 'personal-assets' / 'api-key.txt'
    if api_key_file.exists():
        print("\n⚠️  WARNING: Found api-key.txt with sensitive information!")
        print(f"  Location: {api_key_file}")
        print("  ACTION REQUIRED: Delete this file immediately and rotate all API keys!")
    
    print("\n" + "=" * 50)
    print("Cleanup complete!")
    print("\nREMINDER: Don't forget to:")
    print("1. Delete any api-key.txt files")
    print("2. Rotate all exposed API keys")
    print("3. Update .gitignore to exclude personal-assets")
    print("4. Commit these changes")

if __name__ == "__main__":
    main()