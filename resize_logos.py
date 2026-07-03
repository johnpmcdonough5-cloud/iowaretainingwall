import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Pattern to find the inline style for the logo
pattern = re.compile(r'style="height:\s*56px;\s*width:\s*auto;"')
new_style = 'style="height: 64px; width: auto;"'

for html_file in ROOT.rglob("*.html"):
    text = html_file.read_text(encoding="utf-8")
    
    new_text = pattern.sub(new_style, text)
    
    if new_text != text:
        html_file.write_text(new_text, encoding="utf-8")
        print(f"Resized logos in {html_file.relative_to(ROOT)}")
