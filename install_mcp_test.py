#!/usr/bin/env python3
"""
MCP 서버 설치 테스트 스크립트
특히 Magic MCP 비활성화 검증
"""

import json
import sys
from pathlib import Path

# 프로젝트 루트 설정
sys.path.insert(0, str(Path(__file__).parent))

from setup.components.mcp import MCPComponent

def install_mcp_servers():
    """MCP 서버들 설치 및 Magic 비활성화 검증"""
    
    print("=== MCP 서버 설치 테스트 ===")
    
    # MCP 컴포넌트 초기화
    install_dir = Path.home() / ".gemini"
    mcp_component = MCPComponent(install_dir)
    
    # 설치할 서버 목록 (Magic 포함)
    selected_servers = ['context7', 'sequential', 'magic', 'playwright']
    mcp_component.set_selected_servers(selected_servers)
    
    print(f"선택된 서버: {selected_servers}")
    
    # 설치 설정
    config = {
        'selected_mcp_servers': selected_servers,
        'dry_run': True  # 실제 npm 설치는 건너뛰고 설정만 테스트
    }
    
    # Gemini 설정 로드 또는 생성
    print("\n=== Gemini 설정 초기화 ===")
    settings_path = install_dir / "settings.json"
    
    # 기본 설정 생성
    if not settings_path.exists():
        settings_path.parent.mkdir(parents=True, exist_ok=True)
        settings_path.write_text('{}')
    
    gemini_config, config_path = mcp_component._load_gemini_config()
    if gemini_config is None:
        gemini_config = {}
    
    # 필요한 섹션 보장
    if "mcpServers" not in gemini_config:
        gemini_config["mcpServers"] = {}
    if "_disabledMcpServers" not in gemini_config:
        gemini_config["_disabledMcpServers"] = {}
    
    print("✅ 기본 설정 구조 생성")
    
    # 각 서버 설정
    print("\n=== 서버별 설정 처리 ===")
    configured_count = 0
    
    for server_key in selected_servers:
        server_info = mcp_component.mcp_servers[server_key]
        server_config = mcp_component._load_mcp_server_config(server_key)
        
        if server_config is None:
            print(f"❌ {server_key} 설정 로드 실패")
            continue
        
        # disabled_by_default 플래그 확인
        is_disabled_by_default = server_info.get("disabled_by_default", False)
        target_section = "_disabledMcpServers" if is_disabled_by_default else "mcpServers"
        
        print(f"📋 {server_key}:")
        print(f"   - 비활성화 기본값: {is_disabled_by_default}")
        print(f"   - 대상 섹션: {target_section}")
        
        # 비활성화 섹션 코멘트 추가
        if is_disabled_by_default and "_comment" not in gemini_config["_disabledMcpServers"]:
            gemini_config["_disabledMcpServers"]["_comment"] = f"{server_info['description']} - disabled due to compatibility issues"
            gemini_config["_disabledMcpServers"]["_instructions"] = f"Reason: {server_info.get('disabled_reason', 'Compatibility issues')}. Move to mcpServers section to enable."
        
        # 서버 설정 병합
        mcp_component._merge_mcp_server_config(gemini_config[target_section], server_config, server_key)
        configured_count += 1
        
        if is_disabled_by_default:
            print(f"   ✅ {server_key} → _disabledMcpServers (비활성화)")
        else:
            print(f"   ✅ {server_key} → mcpServers (활성화)")
    
    # 설정 저장
    print(f"\n=== 설정 저장 ===")
    success = mcp_component._save_gemini_config(gemini_config, config_path)
    
    if success:
        print("✅ 설정 저장 성공")
    else:
        print("❌ 설정 저장 실패")
        return False
    
    # 최종 검증
    print(f"\n=== 최종 검증 ===")
    
    # 설정 다시 로드하여 검증
    final_config, _ = mcp_component._load_gemini_config()
    
    print("활성화된 MCP 서버:")
    active_servers = final_config.get("mcpServers", {})
    for server_name in active_servers:
        if server_name not in ["_comment", "_instructions"]:
            print(f"  ✅ {server_name}")
    
    print("\n비활성화된 MCP 서버:")
    disabled_servers = final_config.get("_disabledMcpServers", {})
    for server_name in disabled_servers:
        if server_name not in ["_comment", "_instructions"]:
            print(f"  ⏸️ {server_name}")
            if server_name == "magic":
                print(f"     📝 이유: {disabled_servers.get('_instructions', 'N/A')}")
    
    # Magic 검증
    magic_in_disabled = "magic" in final_config.get("_disabledMcpServers", {})
    magic_in_active = "magic" in final_config.get("mcpServers", {})
    
    if magic_in_disabled and not magic_in_active:
        print(f"\n🎉 SUCCESS: Magic MCP가 올바르게 비활성화됨!")
        return True
    elif magic_in_active and not magic_in_disabled:
        print(f"\n❌ FAIL: Magic MCP가 활성화됨 (비활성화되어야 함)")
        return False
    else:
        print(f"\n❌ FAIL: Magic MCP 상태가 명확하지 않음")
        return False

if __name__ == "__main__":
    success = install_mcp_servers()
    sys.exit(0 if success else 1)