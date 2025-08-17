#!/usr/bin/env python3
"""
Magic MCP 비활성화 테스트 스크립트
v4_beta_sync에서 magic MCP가 올바르게 비활성화되는지 확인
"""

import json
import sys
from pathlib import Path

# 프로젝트 루트 설정
sys.path.insert(0, str(Path(__file__).parent))

from setup.components.mcp import MCPComponent

def test_magic_disable():
    """Magic MCP 비활성화 로직 테스트"""
    
    # MCP 컴포넌트 초기화
    install_dir = Path.home() / ".gemini"
    mcp_component = MCPComponent(install_dir)
    
    print("=== Magic MCP 설정 확인 ===")
    magic_info = mcp_component.mcp_servers['magic']
    
    print(f"이름: {magic_info['name']}")
    print(f"설명: {magic_info['description']}")
    print(f"API 키 필요: {magic_info.get('requires_api_key', False)}")
    print(f"기본 비활성화: {magic_info.get('disabled_by_default', False)}")
    print(f"비활성화 이유: {magic_info.get('disabled_reason', 'N/A')}")
    
    # Magic 서버 설정 로드
    print("\n=== Magic 서버 설정 로드 ===")
    magic_config = mcp_component._load_mcp_server_config('magic')
    
    if magic_config:
        print("✅ Magic 설정 파일 로드 성공")
        print(f"설정 내용: {json.dumps(magic_config, indent=2)}")
    else:
        print("❌ Magic 설정 파일 로드 실패")
        return False
    
    # 시뮬레이션된 Gemini 설정 생성
    print("\n=== 설정 생성 시뮬레이션 ===")
    
    # 기존 설정 로드
    gemini_config, config_path = mcp_component._load_gemini_config()
    if gemini_config is None:
        gemini_config = {}
    
    # mcpServers와 _disabledMcpServers 섹션 보장
    if "mcpServers" not in gemini_config:
        gemini_config["mcpServers"] = {}
    if "_disabledMcpServers" not in gemini_config:
        gemini_config["_disabledMcpServers"] = {}
    
    # Magic 서버 처리
    server_info = mcp_component.mcp_servers['magic']
    is_disabled_by_default = server_info.get("disabled_by_default", False)
    target_section = "_disabledMcpServers" if is_disabled_by_default else "mcpServers"
    
    print(f"Magic은 비활성화 기본값: {is_disabled_by_default}")
    print(f"대상 섹션: {target_section}")
    
    # 비활성화 섹션 코멘트 추가
    if is_disabled_by_default and "_comment" not in gemini_config["_disabledMcpServers"]:
        gemini_config["_disabledMcpServers"]["_comment"] = f"{server_info['description']} - disabled due to compatibility issues"
        gemini_config["_disabledMcpServers"]["_instructions"] = f"Reason: {server_info.get('disabled_reason', 'Compatibility issues')}. Move to mcpServers section to enable."
    
    # 서버 설정 병합
    mcp_component._merge_mcp_server_config(gemini_config[target_section], magic_config, 'magic')
    
    print(f"\n=== 최종 설정 ===")
    print("mcpServers 섹션:")
    print(json.dumps(gemini_config.get("mcpServers", {}), indent=2))
    
    print("\n_disabledMcpServers 섹션:")
    print(json.dumps(gemini_config.get("_disabledMcpServers", {}), indent=2))
    
    # 검증
    if "magic" in gemini_config.get("_disabledMcpServers", {}):
        print("\n✅ SUCCESS: Magic MCP가 _disabledMcpServers 섹션에 올바르게 배치됨")
        return True
    elif "magic" in gemini_config.get("mcpServers", {}):
        print("\n❌ FAIL: Magic MCP가 mcpServers 섹션에 배치됨 (비활성화되지 않음)")
        return False
    else:
        print("\n❌ FAIL: Magic MCP가 어느 섹션에도 없음")
        return False

if __name__ == "__main__":
    success = test_magic_disable()
    sys.exit(0 if success else 1)