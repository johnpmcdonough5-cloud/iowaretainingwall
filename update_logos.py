import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

nav_pattern = re.compile(
    r'<span class="logo-box">Logo</span>\s*<span class="brand-name"\s*><span>Eastern (?:Rataining|Retaining)</span><span>Wall</span></span>',
    re.IGNORECASE
)

footer_pattern = re.compile(
    r'<span class="logo-box">Logo</span>\s*<span>Eastern (?:Rataining|Retaining) Wall</span>',
    re.IGNORECASE
)

for html_file in ROOT.rglob("*.html"):
    text = html_file.read_text(encoding="utf-8")
    
    depth = len(html_file.relative_to(ROOT).parts) - 1
    prefix = "../" * depth if depth > 0 else ""
    
    # Nav replacement (only really needed in _nav.html and templates, but we can do it everywhere)
    new_text = nav_pattern.sub(f'<img src="{prefix}assets/logo.png" alt="Eastern Iowa Retaining Wall" style="height: 42px; width: auto;" />', text)
    
    # Footer replacement
    new_text = footer_pattern.sub(f'<img src="{prefix}assets/logo.png" alt="Eastern Iowa Retaining Wall" style="height: 42px; width: auto;" />', new_text)
    
    if new_text != text:
        html_file.write_text(new_text, encoding="utf-8")
        print(f"Updated {html_file.relative_to(ROOT)}")
