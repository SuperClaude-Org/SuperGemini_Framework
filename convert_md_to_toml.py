#!/usr/bin/env python3
"""
SuperGemini Commands MD to TOML Converter
Converts all .md files in Commands directory to .toml format
"""

import os
from pathlib import Path

def convert_md_to_toml():
    """Convert all MD files to TOML format in Commands directory"""
    
    # Commands 디렉토리 경로
    commands_dir = Path("SuperGemini/Commands")
    
    if not commands_dir.exists():
        print(f"❌ 디렉토리를 찾을 수 없습니다: {commands_dir}")
        return
    
    # 변환 통계
    converted = []
    skipped = []
    errors = []
    
    # 모든 .md 파일 처리
    for md_file in sorted(commands_dir.glob("*.md")):
        toml_file = md_file.with_suffix('.toml')
        
        # 이미 TOML 파일이 존재하는 경우
        if toml_file.exists():
            print(f"⏭️  건너뜀 (이미 존재): {md_file.name} → {toml_file.name}")
            skipped.append(md_file.name)
            continue
        
        try:
            # MD 파일 읽기
            content = md_file.read_text(encoding='utf-8')
            
            # TOML 형식으로 변환 (단순히 prompt 필드에 전체 내용 포함)
            toml_content = f'prompt = """\n{content}\n"""\n'
            
            # TOML 파일로 저장
            toml_file.write_text(toml_content, encoding='utf-8')
            
            print(f"✅ 변환 완료: {md_file.name} → {toml_file.name}")
            converted.append(md_file.name)
            
        except Exception as e:
            print(f"❌ 변환 실패: {md_file.name} - {str(e)}")
            errors.append((md_file.name, str(e)))
    
    # 결과 요약
    print("\n" + "="*50)
    print("📊 변환 결과 요약")
    print("="*50)
    print(f"✅ 성공적으로 변환: {len(converted)}개")
    print(f"⏭️  건너뜀 (이미 존재): {len(skipped)}개")
    print(f"❌ 오류 발생: {len(errors)}개")
    
    if converted:
        print(f"\n변환된 파일:")
        for file in converted:
            print(f"  - {file}")
    
    if errors:
        print(f"\n오류 발생 파일:")
        for file, error in errors:
            print(f"  - {file}: {error}")
    
    print("\n✨ 변환 작업 완료!")

if __name__ == "__main__":
    print("🚀 SuperGemini MD → TOML 변환 시작...")
    print("="*50)
    convert_md_to_toml()