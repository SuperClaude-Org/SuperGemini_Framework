#!/usr/bin/env python3
"""
Test all 6 MCP servers installation
"""

import json
import subprocess
import sys
from pathlib import Path

def test_all_mcp_servers():
    """Test all 6 MCP servers"""
    
    # All 6 MCP servers from v4
    packages = {
        "context7": "@upstash/context7-mcp@latest",
        "sequential": "@modelcontextprotocol/server-sequential-thinking", 
        "magic": "@21st-dev/magic",
        "playwright": "@playwright/mcp@latest",
        "serena": "@serena-ai/mcp-server",
        "morphllm": "@morphllm/fast-apply"
    }
    
    # Server names for settings.json
    server_names = {
        "context7": "context7",
        "sequential": "sequential-thinking",
        "magic": "magic", 
        "playwright": "playwright",
        "serena": "serena",
        "morphllm": "morphllm-fast-apply"
    }
    
    print("=== Testing ALL 6 MCP servers installation ===")
    
    installed_servers = {}
    failed_servers = []
    
    # Test npm installation for all servers
    for server_key, npm_package in packages.items():
        print(f"\nInstalling {server_key}: {npm_package}")
        
        try:
            result = subprocess.run(
                ["npm", "install", "-g", npm_package],
                capture_output=True,
                text=True,
                timeout=180,
                shell=True
            )
            
            if result.returncode == 0:
                print(f"✅ Successfully installed: {npm_package}")
                installed_servers[server_key] = npm_package
            else:
                print(f"❌ Installation failed: {result.stderr}")
                failed_servers.append(server_key)
                
        except Exception as e:
            print(f"❌ Error installing {server_key}: {e}")
            failed_servers.append(server_key)
    
    print(f"\n=== Installation Summary ===")
    print(f"✅ Successfully installed: {len(installed_servers)} servers")
    print(f"❌ Failed installations: {len(failed_servers)} servers")
    
    if failed_servers:
        print(f"Failed servers: {failed_servers}")
    
    # Configure settings.json for successfully installed servers
    if installed_servers:
        print(f"\n=== Configuring settings.json ===")
        
        settings_path = Path.home() / ".gemini" / "settings.json"
        
        try:
            # Load current settings
            with open(settings_path, 'r') as f:
                settings = json.load(f)
            
            # Initialize mcpServers if not exists
            if "mcpServers" not in settings:
                settings["mcpServers"] = {}
            
            # Add each successfully installed server
            for server_key in installed_servers:
                server_name = server_names[server_key]
                npm_package = packages[server_key]
                
                settings["mcpServers"][server_name] = {
                    "command": "npx",
                    "args": ["-y", npm_package]
                }
                print(f"✅ Configured: {server_name}")
            
            # Save updated settings
            with open(settings_path, 'w') as f:
                json.dump(settings, f, indent=2)
            
            print(f"✅ settings.json updated with {len(installed_servers)} servers")
            
            # Show final result
            print(f"\n=== Final Verification ===")
            print(f"MCP servers in settings.json: {list(settings['mcpServers'].keys())}")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to configure settings.json: {e}")
            return False
    
    return False

if __name__ == "__main__":
    print("Testing installation of ALL 6 MCP servers...\n")
    test_all_mcp_servers()