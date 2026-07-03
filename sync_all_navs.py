"""
sync_all_navs.py
────────────────
• Injects the nav from _nav.html into every HTML page.
• Converts ALL absolute paths ( href="/…" / src="/…" ) to paths that are
  relative to each file's depth, so the site works when opened directly
  from the file system (file:// protocol) without a web server.

Run any time _nav.html changes:
    python sync_all_navs.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAV_TEMPLATE = (ROOT / "_nav.html").read_text(encoding="utf-8").strip()

# ── Patterns ────────────────────────────────────────────────────────────────

# Matches the full <header …> … </header> block, plus the optional
# <script src="…nav.js…"></script> that immediately follows it.
HEADER_RE = re.compile(
    r"<header\s[^>]*class=['\"]site-header['\"][^>]*>.*?</header>"
    r"(?:\s*<script[^>]+nav\.js[^>]*>\s*</script>)?",
    re.DOTALL | re.IGNORECASE,
)

# Matches  href="/path"  or  src="/path"  but NOT  href="//"  (protocol-relative)
# Captures: group(1) = attribute + opening quote, group(2) = /path…
ABS_RE = re.compile(r'((?:href|src)=["\'])(\/(?!\/)[^"\']*)')


# ── Helpers ──────────────────────────────────────────────────────────────────

def relativize(html: str, depth: int) -> str:
    """Replace every absolute /path with depth-appropriate ../…/path."""
    prefix = "../" * depth  # e.g. depth 3 → "../../.."
    def _repl(m):
        return m.group(1) + prefix + m.group(2).lstrip("/")
    return ABS_RE.sub(_repl, html)


# ── Main ─────────────────────────────────────────────────────────────────────

updated = skipped = 0

for html_file in sorted(ROOT.rglob("*.html")):
    # Skip partial/template files and hidden directories
    if html_file.name.startswith("_"):
        continue
    if any(part.startswith(".") for part in html_file.parts):
        continue

    text      = html_file.read_text(encoding="utf-8")
    depth     = len(html_file.relative_to(ROOT).parts) - 1  # dirs from root
    rel_label = html_file.relative_to(ROOT)

    if not HEADER_RE.search(text):
        print(f"  skip (no header): {rel_label}")
        skipped += 1
        continue

    # 1. Build a depth-correct version of the nav
    nav_relativized = relativize(NAV_TEMPLATE, depth)

    # 2. Swap old header (+ any existing nav.js script tag) for the new nav
    new_text = HEADER_RE.sub(nav_relativized, text, count=1)

    # 3. Relativize every other absolute path still in the file
    #    (stylesheet link, images in body, in-content hrefs, etc.)
    new_text = relativize(new_text, depth)

    if new_text == text:
        print(f"  unchanged:        {rel_label}")
        continue

    html_file.write_text(new_text, encoding="utf-8")
    print(f"  updated (d={depth}):   {rel_label}")
    updated += 1

print(f"\nDone — {updated} file(s) updated, {skipped} skipped (no header).")
