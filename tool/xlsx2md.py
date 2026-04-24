#!/usr/bin/env python3
import subprocess
import argparse
import sys
import re
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("Error: pandas required. Install: pip install pandas")
    sys.exit(1)


def clean_markdown(content, fill_empty=''):
    lines = content.split('\n')
    fixed_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        if '|' in line and i + 1 < len(lines) and set(lines[i + 1].replace('|', '').replace('-', '').replace(':', '').strip()) <= set(''):
            table_lines = []
            while i < len(lines) and '|' in lines[i]:
                table_lines.append(lines[i])
                i += 1
            fixed_lines.extend(clean_table(table_lines, fill_empty))
        else:
            fixed_lines.append(line)
            i += 1

    return '\n'.join(fixed_lines)


def clean_table(table_lines, fill_empty):
    headers = [h.strip() for h in table_lines[0].split('|')[1:-1]]

    data_rows = []
    for line in table_lines[2:]:
        cells = [c.strip() for c in line.split('|')[1:-1]]
        while len(cells) < len(headers):
            cells.append('')
        data_rows.append(cells[:len(headers)])

    df = pd.DataFrame(data_rows, columns=headers)
    df = df.replace(['NaN', 'nan', ''], fill_empty).fillna(fill_empty)

    df.columns = [
        ' ' if re.match(r'^Unnamed:\s*\d+$', str(col)) else col
        for col in df.columns
    ]

    df = df[~df.apply(lambda row: all(str(v).strip() == '' for v in row), axis=1)]

    return df_to_md(df)


def df_to_md(df):
    headers = [str(h) for h in df.columns]
    lines = [
        '| ' + ' | '.join(headers) + ' |',
        '|' + '|'.join(['---'] * len(headers)) + '|'
    ]
    for _, row in df.iterrows():
        lines.append('| ' + ' | '.join(str(v) for v in row) + ' |')
    return lines


def excel_to_clean_md(input_file, output_file=None):
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)

    output_path = Path(output_file) if output_file else input_path.with_suffix('.md')

    print(f"Converting {input_path.name} to Markdown...")
    result = subprocess.run(
        ['markitdown', str(input_path)],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"markitdown failed: {result.stderr}")
        sys.exit(1)

    print("Cleaning NaN and Unnamed columns...")
    cleaned = clean_markdown(result.stdout)

    output_path.write_text(cleaned, encoding='utf-8')
    print(f"\nDone! Output: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert Excel to clean Markdown (removes NaN and Unnamed columns)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s file.xlsx                    # Convert to file.md
  %(prog)s file.xlsx -o output.md       # Specify output file
        """
    )
    parser.add_argument('input', help='Input Excel file (.xlsx)')
    parser.add_argument('-o', '--output', help='Output Markdown file')
    args = parser.parse_args()
    excel_to_clean_md(args.input, args.output)


if __name__ == '__main__':
    main()
