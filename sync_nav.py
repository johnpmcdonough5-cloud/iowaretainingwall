import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAV = (ROOT / "_nav.html").read_text(encoding="utf-8")
pattern = re.compile(r"<header class=\"site-header\">.*?</header>", re.DOTALL)

for html_file in ROOT.rglob("*.html"):
    if html_file.name.startswith("_"):
        continue
    text = html_file.read_text(encoding="utf-8")
    if not pattern.search(text):
        continue
    html_file.write_text(pattern.sub(NAV.strip(), text, count=1), encoding="utf-8")
    print(f"synced: {html_file.relative_to(ROOT)}")
