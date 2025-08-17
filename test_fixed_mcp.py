#!/usr/bin/env python3
"""
Test fixed MCP installation with proper Serena (uv) and Morphllm (corrected npm)
"""

import sys
from pathlib import Path

# Add setup to path
current_dir = Path(__file__).parent
setup_dir = current_dir / "setup"
sys.path.insert(0, str(setup_dir))

from setup.components.mcp import MCPComponent
from setup.utils.logger import setup_logging, get_logger

def test_fixed_mcp_installation():
    """Test fixed MCP component installation with all 6 servers"""
    setup_logging("mcp_fixed_test")
    logger = get_logger()
    
    install_dir = Path.home() / ".gemini"
    
    print("=== 수정된 MCP 설치 시스템 테스트 ===")
    print(f"설치 디렉토리: {install_dir}")
    
    # Create MCP component instance
    mcp = MCPComponent(install_dir)
    
    # Test all 6 servers
    all_servers = ["context7", "sequential", "magic", "playwright", "serena", "morphllm"]
    mcp.set_selected_servers(all_servers)
    
    print(f"선택된 MCP 서버들: {all_servers}")
    
    # Show server details
    print("\n=== 서버 설치 방법 확인 ===")
    for server_key in all_servers:
        server_info = mcp.mcp_servers[server_key]
        install_method = server_info.get("install_method", "npm")
        
        if install_method == "uv":
            package = server_info.get("uv_package", "N/A")
            print(f"{server_key}: uv 설치 - {package}")
        else:
            package = server_info.get("npm_package", "N/A")
            print(f"{server_key}: npm 설치 - {package}")
    
    # Check prerequisites
    print("\n=== 전제 조건 검증 ===")
    success, errors = mcp.validate_prerequisites()
    if not success:
        print(f"전제 조건 실패: {errors}")
        return False
    
    print("✅ 모든 전제 조건 검증 성공")
    
    # Check additional prerequisites (npm, uv)
    success, errors = mcp._validate_prerequisites()
    if not success:
        for error in errors:
            print(f"❌ {error}")
    else:
        print("✅ npm 및 uv 전제 조건 검증 성공")
    
    # Test installation
    config = {
        "selected_mcp_servers": all_servers,
        "force": True,
        "backup": False,
        "dry_run": False
    }
    
    print("\n=== MCP 설치 시작 ===")
    success = mcp._install(config)
    
    if success:
        print("🎉 MCP 설치 성공!")
        
        # Check final settings.json
        settings_path = install_dir / "settings.json"
        if settings_path.exists():
            print(f"✅ settings.json 존재: {settings_path}")
            with open(settings_path, 'r') as f:
                content = f.read()
                print(f"\n최종 설정 내용:\n{content}")
        else:
            print("❌ settings.json 없음")
            
    else:
        print("❌ MCP 설치 실패")
    
    return success

if __name__ == "__main__":
    test_fixed_mcp_installation()