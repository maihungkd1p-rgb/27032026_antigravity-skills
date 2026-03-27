"""
RAG Knowledge Cleaner Script
Cleans PDF conversion noise from Markdown artifacts.

Usage:
    python clean_pdf_noise.py [knowledge_dir]
    
Example:
    python clean_pdf_noise.py C:\path\to\knowledge
"""
import re
from pathlib import Path
import argparse

def clean_markdown(content: str) -> str:
    """Clean PDF conversion noise from markdown content."""
    
    # Remove page markers: \-\-- Trang XX \-\--\
    content = re.sub(r'\\-\\-- Trang \d+ \\-\\--\\?\r?\n?', '', content)
    
    # Alternative page marker formats
    content = re.sub(r'---\s*Trang\s*\d+\s*---\r?\n?', '', content)
    content = re.sub(r'\*\*Trang \d+\*\*\r?\n?', '', content)
    
    # Remove escape sequences for dashes
    content = re.sub(r'\\-\\--', '---', content)
    
    # Remove trailing backslashes at end of lines
    content = re.sub(r'\\\r?\n', '\n', content)
    
    # Normalize line endings (CRLF -> LF)
    content = content.replace('\r\n', '\n')
    content = content.replace('\r', '\n')
    
    # Remove escape backslashes before special chars
    content = re.sub(r'\\\.\.\.', '...', content)
    content = re.sub(r'\\&', '&', content)
    
    # Clean multiple blank lines (more than 2)
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    # Remove grid table formatting
    content = re.sub(r'\+[-=]+\+', '', content)
    
    # Clean leading/trailing whitespace
    content = content.strip()
    
    return content

def process_file(file_path: Path, dry_run: bool = False) -> int:
    """Process a single markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        cleaned = clean_markdown(content)
        
        if content != cleaned:
            chars_removed = len(content) - len(cleaned)
            if not dry_run:
                file_path.write_text(cleaned, encoding='utf-8')
                print(f"✓ Cleaned: {file_path.name} (-{chars_removed} chars)")
            else:
                print(f"○ Would clean: {file_path.name} (-{chars_removed} chars)")
            return chars_removed
        else:
            print(f"○ Skipped: {file_path.name} (already clean)")
            return 0
    except Exception as e:
        print(f"✗ Error: {file_path.name} - {e}")
        return 0

def main():
    parser = argparse.ArgumentParser(description='Clean PDF noise from markdown artifacts')
    parser.add_argument('knowledge_dir', help='Path to knowledge directory')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing')
    args = parser.parse_args()
    
    base = Path(args.knowledge_dir)
    
    if not base.exists():
        print(f"Error: Directory not found: {base}")
        return
    
    total_cleaned = 0
    files_processed = 0
    
    # Process all knowledge items
    for ki_dir in base.iterdir():
        if ki_dir.is_dir() and not ki_dir.name.startswith('.'):
            artifacts_dir = ki_dir / "artifacts"
            if artifacts_dir.exists():
                print(f"\n=== {ki_dir.name} ===")
                for md_file in artifacts_dir.glob("*.md"):
                    chars = process_file(md_file, args.dry_run)
                    total_cleaned += chars
                    files_processed += 1
    
    print(f"\n{'='*40}")
    print(f"Total files processed: {files_processed}")
    print(f"Total characters {'would be ' if args.dry_run else ''}removed: {total_cleaned}")
    print("Done!" if not args.dry_run else "Dry run complete.")

if __name__ == "__main__":
    main()
