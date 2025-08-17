#!/usr/bin/env python3
"""
Test only Serena and Morphllm installation specifically
"""

import json
import subprocess
import sys
from pathlib import Path

def test_serena_installation():
    """Test Serena installation using uv"""
    print("=== Serena (uv) 설치 테스트 ===")
    
    try:
        # Try the exact command from web search results
        result = subprocess.run(
            ["uv", "tool", "install", "--from", "git+https://github.com/oraios/serena", "serena-agent"],
            capture_output=True,
            text=True,
            timeout=300,
            shell=True
        )
        
        if result.returncode == 0:
            print("✅ Serena 설치 성공")
            print(f"Output: {result.stdout}")
            return True
        else:
            print(f"❌ Serena 설치 실패: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Serena 설치 오류: {e}")
        return False

def test_morphllm_installation():
    """Test Morphllm installation using npm"""
    print("\n=== Morphllm (npm) 설치 테스트 ===")
    
    try:
        result = subprocess.run(
            ["npm", "install", "-g", "@morph-llm/morph-fast-apply"],
            capture_output=True,
            text=True,
            timeout=180,
            shell=True
        )
        
        if result.returncode == 0:
            print("✅ Morphllm 설치 성공")
            return True
        else:
            print(f"❌ Morphllm 설치 실패: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Morphllm 설치 오류: {e}")
        return False

def test_settings_configuration():
    """Test adding both servers to settings.json"""
    print("\n=== settings.json 구성 테스트 ===")
    
    settings_path = Path.home() / ".gemini" / "settings.json"
    
    try:
        # Load current settings
        with open(settings_path, 'r') as f:
            settings = json.load(f)
        
        # Ensure mcpServers exists
        if "mcpServers" not in settings:
            settings["mcpServers"] = {}
        
        # Add Serena server
        settings["mcpServers"]["serena"] = {
            "command": "uv",
            "args": ["tool", "run", "serena", "start-mcp-server", "--context", "ide-assistant"]
        }
        
        # Add Morphllm server
        settings["mcpServers"]["morphllm-fast-apply"] = {
            "command": "npx",
            "args": ["-y", "@morph-llm/morph-fast-apply", "/app/"],
            "env": {
                "MORPH_API_KEY": "",
                "ALL_TOOLS": "true"
            }
        }
        
        # Save settings
        with open(settings_path, 'w') as f:
            json.dump(settings, f, indent=2)
        
        print("✅ settings.json 구성 성공")
        print(f"MCP 서버들: {list(settings['mcpServers'].keys())}")
        
        return True
        
    except Exception as e:
        print(f"❌ settings.json 구성 실패: {e}")
        return False

def verify_installation():
    """Verify both tools are available"""
    print("\n=== 설치 검증 ===")
    
    # Check Serena
    try:
        result = subprocess.run(
            ["uv", "tool", "list"],
            capture_output=True,
            text=True,
            timeout=30,
            shell=True
        )
        
        if result.returncode == 0 and "serena" in result.stdout:
            print("✅ Serena 검증 성공")
        else:
            print("❌ Serena 검증 실패")
            
    except Exception as e:
        print(f"❌ Serena 검증 오류: {e}")
    
    # Check Morphllm
    try:
        result = subprocess.run(
            ["npm", "list", "-g", "@morph-llm/morph-fast-apply"],
            capture_output=True,
            text=True,
            timeout=30,
            shell=True
        )
        
        if result.returncode == 0:
            print("✅ Morphllm 검증 성공")
        else:
            print("❌ Morphllm 검증 실패")
            
    except Exception as e:
        print(f"❌ Morphllm 검증 오류: {e}")

if __name__ == "__main__":
    print("Serena와 Morphllm 개별 설치 테스트 시작\n")
    
    # Test individual installations
    serena_ok = test_serena_installation()
    morphllm_ok = test_morphllm_installation()
    
    if serena_ok and morphllm_ok:
        # Configure settings.json
        config_ok = test_settings_configuration()
        
        if config_ok:
            # Verify installations
            verify_installation()
            print("\n🎉 모든 테스트 완료!")
        else:
            print("\n❌ 설정 단계에서 실패")
    else:
        print(f"\n❌ 설치 실패 - Serena: {serena_ok}, Morphllm: {morphllm_ok}")