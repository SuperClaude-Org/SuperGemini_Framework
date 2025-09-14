#!/usr/bin/env python3
"""
Qwen Framework Installation Script
"""

import os
import sys
import shutil
from pathlib import Path

def install_qwen_framework():
    """Install Qwen framework components to .qwen directory"""
    # Get the current directory
    current_dir = Path(__file__).parent.absolute()
    qwen_dir = Path(".qwen").absolute()
    
    # Create .qwen directory if it doesn't exist
    qwen_dir.mkdir(exist_ok=True)
    
    # Copy commands
    commands_src = current_dir / "SuperQwen" / "Commands"
    commands_dst = qwen_dir / "commands"
    commands_dst.mkdir(exist_ok=True)
    
    if commands_src.exists():
        for file in commands_src.glob("*.toml"):
            shutil.copy2(file, commands_dst)
        print(f"✓ Copied {len(list(commands_src.glob('*.toml')))} command files")
    else:
        print(f"⚠️  Commands source directory not found: {commands_src}")
    
    # Copy modes
    modes_src = current_dir / "SuperQwen" / "Modes"
    modes_dst = qwen_dir / "modes"
    modes_dst.mkdir(exist_ok=True)
    
    if modes_src.exists():
        for file in modes_src.glob("*.md"):
            shutil.copy2(file, modes_dst)
        print(f"✓ Copied {len(list(modes_src.glob('*.md')))} mode files")
    else:
        print(f"⚠️  Modes source directory not found: {modes_src}")
    
    # Copy agents
    agents_src = current_dir / "SuperQwen" / "Agents"
    agents_dst = qwen_dir / "agents"
    agents_dst.mkdir(exist_ok=True)
    
    if agents_src.exists():
        for file in agents_src.glob("*.md"):
            shutil.copy2(file, agents_dst)
        print(f"✓ Copied {len(list(agents_src.glob('*.md')))} agent files")
    else:
        print(f"⚠️  Agents source directory not found: {agents_src}")
    
    print(f"\n✅ Qwen Framework installed successfully to {qwen_dir}")
    print("\nTo use the framework:")
    print("1. Restart your Qwen CLI session")
    print("2. Use commands like /qwen:analyze, /qwen:implement, etc.")
    print("3. Enable modes by using the appropriate flags")

if __name__ == "__main__":
    install_qwen_framework()