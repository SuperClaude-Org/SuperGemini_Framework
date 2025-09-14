#!/usr/bin/env python3
"""
Qwen Framework Setup Script
"""

import os
import sys
import json
from pathlib import Path

def setup_qwen_framework():
    """Setup Qwen framework with default configuration"""
    # Get the .qwen directory
    qwen_dir = Path(".qwen").absolute()
    qwen_dir.mkdir(exist_ok=True)
    
    # Create or update settings.json
    settings_file = qwen_dir / "settings.json"
    
    # Default settings with MCP servers
    default_settings = {
        "mcpServers": {
            "serena": {
                "command": "uvx",
                "args": [
                    "--from",
                    "git+https://github.com/oraios/serena",
                    "serena",
                    "start-mcp-server",
                    "--context",
                    "ide-assistant",
                    "--project",
                    str(Path.cwd())
                ]
            },
            "context7": {
                "command": "uvx",
                "args": [
                    "context7-mcp-server",
                    "start"
                ]
            },
            "sequential": {
                "command": "uvx",
                "args": [
                    "sequential-mcp-server",
                    "start"
                ]
            }
        }
    }
    
    # Write settings
    with open(settings_file, "w") as f:
        json.dump(default_settings, f, indent=2)
    
    print(f"✅ Qwen Framework settings configured at {settings_file}")
    print("\nMCP Servers configured:")
    for server in default_settings["mcpServers"]:
        print(f"  - {server}")

if __name__ == "__main__":
    setup_qwen_framework()