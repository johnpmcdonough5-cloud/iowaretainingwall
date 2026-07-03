import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent

for html_file in ROOT.rglob("*.html"):
    text = html_file.read_text(encoding="utf-8")
    
    # Replace "Denver, Colorado" first to avoid "Eastern Iowa, Colorado"
    new_text = text.replace("Denver, Colorado", "Eastern Iowa")
    new_text = new_text.replace("Denver, CO", "Eastern Iowa")
    
    # Replace remaining "Denver"
    new_text = new_text.replace("Denver", "Eastern Iowa")
    
    if new_text != text:
        html_file.write_text(new_text, encoding="utf-8")
        print(f"Updated {html_file.relative_to(ROOT)}")
