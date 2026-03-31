#!/usr/bin/env python3
import re
from pathlib import Path

def format_md_file(file_path):
    content = file_path.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    new_lines = []
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        
        if line_stripped:
            line_stripped = re.sub(r'说\s{2,}明', '说明', line_stripped)
            line_stripped = re.sub(r'[\u3000\xa0]+', ' ', line_stripped)
        
        new_lines.append(line_stripped)
    
    content = '\n'.join(new_lines)
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    content = re.sub(r'^(\d+)\.\s*【(强制|推荐|可选)】(.+)$', r'\1. **\2** \3', content, flags=re.MULTILINE)
    
    return content

def process_file(file_path):
    print(f"  📝 处理: {file_path.name}")
    
    try:
        original = file_path.read_text(encoding='utf-8')
        formatted = format_md_file(file_path)
        
        if formatted != original:
            file_path.write_text(formatted, encoding='utf-8')
            print(f"    ✅ 格式化完成")
        else:
            print(f"    ⏭️  无需格式化")
            
    except Exception as e:
        print(f"    ❌ 失败: {str(e)}")

def main():
    target_dir = Path("/Users/hongyaotang/src/harness_engineering/现有规范/基础层规范")
    
    print(f"📂 目标目录: {target_dir}")
    print("=" * 50)
    
    md_files = list(target_dir.rglob("*.md"))
    
    if not md_files:
        print("未找到 md 文件")
        return
    
    print(f"📋 找到 {len(md_files)} 个 md 文件\n")
    
    for f in md_files:
        process_file(f)
    
    print("\n" + "=" * 50)
    print("✅ 格式化完成")

if __name__ == "__main__":
    main()
