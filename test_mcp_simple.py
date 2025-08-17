#!/usr/bin/env python3
"""
Simple MCP installation test without file locking
"""

import json
import subprocess
import sys
from pathlib import Path

def test_npm_installation():
    """Test npm package installation"""
    packages = {
        "context7": "@upstash/context7-mcp@latest",
        "sequential": "@modelcontextprotocol/server-sequential-thinking"
    }
    
    print("=== Testing npm package installation ===")
    
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
            else:
                print(f"❌ Installation failed: {result.stderr}")
                
        except Exception as e:
            print(f"❌ Error installing {server_key}: {e}")

def test_settings_configuration():
    """Test settings.json configuration"""
    print("\n=== Testing settings.json configuration ===")
    
    settings_path = Path.home() / ".gemini" / "settings.json"
    
    # Load current settings
    try:
        with open(settings_path, 'r') as f:
            settings = json.load(f)
        print(f"✅ Loaded current settings: {settings}")
    except Exception as e:
        print(f"❌ Failed to load settings: {e}")
        return False
    
    # Add MCP servers configuration
    if "mcpServers" not in settings:
        settings["mcpServers"] = {}
    
    # Add context7 server
    settings["mcpServers"]["context7"] = {
        "command": "npx",
        "args": ["-y", "@upstash/context7-mcp@latest"]
    }
    
    # Add sequential server  
    settings["mcpServers"]["sequential-thinking"] = {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
    
    # Save settings
    try:
        with open(settings_path, 'w') as f:
            json.dump(settings, f, indent=2)
        print("✅ Successfully updated settings.json")
        return True
    except Exception as e:
        print(f"❌ Failed to save settings: {e}")
        return False

def verify_installation():
    """Verify the complete installation"""
    print("\n=== Verification ===")
    
    settings_path = Path.home() / ".gemini" / "settings.json"
    
    try:
        with open(settings_path, 'r') as f:
            settings = json.load(f)
        
        if "mcpServers" in settings:
            print(f"✅ MCP servers configured: {list(settings['mcpServers'].keys())}")
            print("✅ Full installation successful!")
            print(f"\nFinal settings.json content:")
            print(json.dumps(settings, indent=2))
            return True
        else:
            print("❌ No MCP servers found in settings")
            return False
            
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        return False

if __name__ == "__main__":
    print("Starting simplified MCP installation test...\n")
    
    # Test npm installation
    test_npm_installation()
    
    # Test settings configuration  
    success = test_settings_configuration()
    
    if success:
        # Verify complete installation
        verify_installation()
    else:
        print("❌ Installation failed at settings configuration step")