#!/usr/bin/env python
"""Convert SuperGemini MD command files to Gemini CLI TOML format."""

import os
import re
from pathlib import Path

def extract_front_matter(content):
    """Extract YAML front matter from MD file."""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        front_matter = match.group(1)
        content_without_fm = content[match.end():]
        
        # Extract description
        desc_match = re.search(r'description:\s*"([^"]+)"', front_matter)
        description = desc_match.group(1) if desc_match else ""
        
        return description, content_without_fm
    return "", content

def convert_md_to_toml(md_content):
    """Convert MD content to TOML format."""
    description, main_content = extract_front_matter(md_content)
    
    # Clean up the content - remove Gemini Code specific sections
    main_content = re.sub(r'## Gemini Code Integration.*', '', main_content, flags=re.DOTALL)
    
    # Build the prompt
    prompt = f"SuperGemini {main_content.strip()}"
    
    # Create TOML content
    toml_content = f'''prompt = """{prompt}"""

description = "{description}"'''
    
    return toml_content

def main():
    md_dir = Path.home() / ".gemini/commands/sc"
    
    # Process all MD files
    for md_file in md_dir.glob("*.md"):
        print(f"Converting {md_file.name}...")
        
        # Read MD file
        with open(md_file, 'r') as f:
            md_content = f.read()
        
        # Convert to TOML
        toml_content = convert_md_to_toml(md_content)
        
        # Write TOML file
        toml_file = md_file.with_suffix('.toml')
        with open(toml_file, 'w') as f:
            f.write(toml_content)
        
        print(f"  Created {toml_file.name}")

if __name__ == "__main__":
    main()