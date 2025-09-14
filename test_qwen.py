#!/usr/bin/env python3
"""
Qwen Framework Test Script
"""

import os
import sys
import json
from pathlib import Path

def test_qwen_framework():
    """Test Qwen framework installation and configuration"""
    print("🔍 Testing Qwen Framework installation...\n")
    
    # Get the .qwen directory
    qwen_dir = Path(".qwen").absolute()
    
    if not qwen_dir.exists():
        print("❌ Qwen Framework not found")
        return False
    
    print(f"✅ Found Qwen Framework at {qwen_dir}")
    
    # Check commands
    commands_dir = qwen_dir / "commands"
    if commands_dir.exists():
        command_files = list(commands_dir.glob("*.toml"))
        print(f"✅ Found {len(command_files)} command files")
        if len(command_files) > 0:
            print(f"   Sample commands: {command_files[0].name}, {command_files[1].name}, ...")
    else:
        print("❌ Commands directory not found")
        return False
    
    # Check modes
    modes_dir = qwen_dir / "modes"
    if modes_dir.exists():
        mode_files = list(modes_dir.glob("*.md"))
        print(f"✅ Found {len(mode_files)} mode files")
        if len(mode_files) > 0:
            print(f"   Sample modes: {mode_files[0].name}, {mode_files[1].name}, ...")
    else:
        print("❌ Modes directory not found")
        return False
    
    # Check agents
    agents_dir = qwen_dir / "agents"
    if agents_dir.exists():
        agent_files = list(agents_dir.glob("*.md"))
        print(f"✅ Found {len(agent_files)} agent files")
        if len(agent_files) > 0:
            print(f"   Sample agents: {agent_files[0].name}, {agent_files[1].name}, ...")
    else:
        print("❌ Agents directory not found")
        return False
    
    # Check settings
    settings_file = qwen_dir / "settings.json"
    if settings_file.exists():
        try:
            with open(settings_file, "r") as f:
                settings = json.load(f)
            print("✅ Settings file found and valid")
            if "mcpServers" in settings:
                servers = list(settings["mcpServers"].keys())
                print(f"   MCP Servers: {', '.join(servers)}")
        except Exception as e:
            print(f"❌ Error reading settings file: {e}")
            return False
    else:
        print("❌ Settings file not found")
        return False
    
    print("\n🎉 All tests passed! Qwen Framework is ready to use.")
    print("\nTo use the framework in Qwen CLI:")
    print("1. Restart your Qwen CLI session")
    print("2. Use commands like /qwen:analyze, /qwen:implement, etc.")
    print("3. Enable modes with flags like --brainstorm, --introspect, etc.")
    
    return True

if __name__ == "__main__":
    test_qwen_framework()
