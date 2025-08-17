#!/usr/bin/env python3
"""Debug uninstall recursion issue"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import with high recursion limit for debugging
sys.setrecursionlimit(10000)

from setup.cli.commands.uninstall import run
import argparse
from pathlib import Path

args = argparse.Namespace(
    complete=True,
    yes=True,
    install_dir=Path.home() / '.gemini',
    dry_run=False,
    quiet=False,
    verbose=False,
    force=False,
    keep_backups=False,
    keep_logs=False,
    keep_settings=False,
    cleanup_env=False,
    no_restore_script=False,
    components=None,
    no_confirm=False
)

print("Starting uninstall test...")
try:
    result = run(args)
    print(f"Uninstall result: {result}")
except RecursionError as e:
    import traceback
    print("RecursionError occurred!")
    traceback.print_exc()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()