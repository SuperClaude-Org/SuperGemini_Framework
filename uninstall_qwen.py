#!/usr/bin/env python3
"""
Qwen Framework Uninstall Script
"""

import os
import sys
import shutil
from pathlib import Path

def uninstall_qwen_framework():
    """Remove Qwen framework components from .qwen directory"""
    # Get the .qwen directory
    qwen_dir = Path(".qwen").absolute()
    
    if not qwen_dir.exists():
        print("ℹ️  Qwen Framework not found")
        return
    
    # Remove commands
    commands_dir = qwen_dir / "commands"
    if commands_dir.exists():
        shutil.rmtree(commands_dir)
        print("✓ Removed commands directory")
    
    # Remove modes
    modes_dir = qwen_dir / "modes"
    if modes_dir.exists():
        shutil.rmtree(modes_dir)
        print("✓ Removed modes directory")
    
    # Remove agents
    agents_dir = qwen_dir / "agents"
    if agents_dir.exists():
        shutil.rmtree(agents_dir)
        print("✓ Removed agents directory")
    
    print(f"\n✅ Qwen Framework uninstalled from {qwen_dir}")

if __name__ == "__main__":
    uninstall_qwen_framework()