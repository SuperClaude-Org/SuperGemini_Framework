#!/usr/bin/env python3
"""
Commands 컴포넌트 직접 설치 테스트
"""

import sys
from pathlib import Path

# 프로젝트 루트 설정
sys.path.insert(0, str(Path(__file__).parent))

from setup.components.commands import CommandsComponent

def install_commands():
    """Commands 컴포넌트 직접 설치"""
    
    print("=== Commands 컴포넌트 설치 테스트 ===")
    
    # Commands 컴포넌트 초기화
    install_dir = Path.home() / ".gemini"
    commands_component = CommandsComponent(install_dir)
    
    print(f"설치 디렉토리: {install_dir}")
    print(f"소스 디렉토리: {commands_component._get_source_dir()}")
    
    # 설치 설정
    config = {
        'dry_run': False,
        'force': True
    }
    
    try:
        # 설치 실행
        print("\n=== 설치 시작 ===")
        success = commands_component._install(config)
        
        if success:
            print("✅ Commands 컴포넌트 설치 성공")
            
            # 설치된 파일 확인
            commands_dir = install_dir / "commands" / "sg"
            if commands_dir.exists():
                toml_files = list(commands_dir.glob("*.toml"))
                print(f"📁 설치된 TOML 파일: {len(toml_files)}개")
                
                # analyze.toml 내용 확인
                analyze_file = commands_dir / "analyze.toml"
                if analyze_file.exists():
                    content = analyze_file.read_text()
                    if "@~/.gemini/agents/" in content:
                        print("✅ analyze.toml이 최신 버전으로 설치됨 (새로운 agents 경로)")
                    else:
                        print("⚠️ analyze.toml이 구버전으로 설치됨 (이전 agents 경로)")
                        print("첫 10줄:")
                        lines = content.split('\n')[:10]
                        for i, line in enumerate(lines, 1):
                            print(f"  {i:2d}: {line}")
                else:
                    print("❌ analyze.toml 파일이 없음")
            else:
                print("❌ commands/sg 디렉토리가 없음")
                
        else:
            print("❌ Commands 컴포넌트 설치 실패")
            return False
            
    except Exception as e:
        print(f"❌ 설치 중 오류 발생: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = install_commands()
    sys.exit(0 if success else 1)