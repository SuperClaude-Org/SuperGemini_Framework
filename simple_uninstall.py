#!/usr/bin/env python3
"""Simple uninstall script for SuperGemini"""

import shutil
from pathlib import Path

def simple_uninstall():
    """Perform simple uninstall by removing .gemini directory"""
    gemini_dir = Path.home() / '.gemini'
    
    if gemini_dir.exists():
        print(f"Removing {gemini_dir}...")
        try:
            shutil.rmtree(gemini_dir)
            print("✅ SuperGemini uninstalled successfully!")
            return 0
        except Exception as e:
            print(f"❌ Error removing directory: {e}")
            return 1
    else:
        print("⚠️ No SuperGemini installation found")
        return 0

if __name__ == "__main__":
    exit(simple_uninstall())