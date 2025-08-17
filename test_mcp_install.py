#!/usr/bin/env python3
"""
Test script for MCP installation
Modified v4 MCP installation test
"""

import sys
from pathlib import Path

# Add setup to path
current_dir = Path(__file__).parent
setup_dir = current_dir / "setup"
sys.path.insert(0, str(setup_dir))

from setup.components.mcp import MCPComponent
from setup.utils.logger import setup_logging, get_logger

def test_mcp_installation():
    """Test MCP component installation"""
    setup_logging("mcp_test")
    logger = get_logger()
    
    # Set up install directory
    install_dir = Path.home() / ".gemini"
    
    print(f"Testing MCP installation to: {install_dir}")
    
    # Create MCP component instance
    mcp = MCPComponent(install_dir)
    
    # Set selected servers (context7, sequential for testing)
    selected_servers = ["context7", "sequential"]
    mcp.set_selected_servers(selected_servers)
    
    print(f"Selected MCP servers: {selected_servers}")
    
    # Check prerequisites
    success, errors = mcp.validate_prerequisites()
    if not success:
        print(f"Prerequisites failed: {errors}")
        return False
    
    print("Prerequisites validated successfully")
    
    # Test installation
    config = {
        "selected_mcp_servers": selected_servers,
        "force": True,
        "backup": False,
        "dry_run": False
    }
    
    print("Starting MCP installation...")
    success = mcp._install(config)
    
    if success:
        print("✅ MCP installation successful!")
        
        # Check settings.json
        settings_path = install_dir / "settings.json"
        if settings_path.exists():
            print(f"✅ settings.json exists at: {settings_path}")
            with open(settings_path, 'r') as f:
                content = f.read()
                print(f"Settings content:\n{content}")
        else:
            print("❌ settings.json not found")
            
    else:
        print("❌ MCP installation failed")
    
    return success

if __name__ == "__main__":
    test_mcp_installation()