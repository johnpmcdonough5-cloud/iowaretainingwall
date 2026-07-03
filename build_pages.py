import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAV = (ROOT / "_nav.html").read_text(encoding="utf-8")
TEMPLATE = (ROOT / "_service_template.html").read_text(encoding="utf-8")

SERVICE_PAGES = {
    "Hardscaping/Retaining Walls/Materials/Gabion Walls/index.html": {
        "TITLE": "Gabion Retaining Walls",
        "HERO_H1": "Builders &amp; Designers of Gabion Retaining Walls",
        "HERO_SUB": "Stone-filled baskets for rugged texture, drainage-friendly performance, and a distinctive modern landscape look.",
        "S1_H2": "Gabion retaining wall contractors throughout the area",
        "S1_P1": "Gabion retaining walls use wire baskets filled with stone to create a strong, permeable wall with a more organic appearance than many masonry systems.",
        "S1_P2": "They work especially well where the design calls for visible stone texture, drainage movement, and a landscape feature that feels substantial without looking overly polished.",
        "S2_H2": "Why gabion retaining walls stand out",
        "S2_P1": "Gabion walls offer excellent visual texture with natural stone fill and a permeable structure that helps manage water movement.",
        "S2_P2": "Placeholder content — replace this section with your final service copy and project photos.",
        "IMG1": "Gabion Retaining Wall",
        "IMG2": "Gabion Wall Project",
    },
    "Hardscaping/Retaining Walls/Materials/Stone Veneer Walls/index.html": {
        "TITLE": "Stone Veneer Retaining Walls",
        "HERO_H1": "Builders &amp; Designers of Stone Veneer Retaining Walls",
        "HERO_SUB": "A refined stone finish over a strong wall structure for upscale patios, entries, and outdoor living areas.",
        "S1_H2": "Stone veneer retaining wall contractors throughout the area",
        "S1_P1": "Stone veneer retaining walls offer the look of natural stone while allowing the core wall structure to be built for the needs of the site.",
        "S1_P2": "This option is ideal when the finished face of the wall matters as much as the support behind it, especially near patios, stairs, seating areas, and front entries.",
        "S2_H2": "Why stone veneer retaining walls are worth the investment",
        "S2_P1": "A premium finished appearance pairs with flexible design options for traditional, rustic, or modern landscapes.",
        "S2_P2": "Placeholder content — replace this section with your final service copy and project photos.",
        "IMG1": "Stone Veneer Wall",
        "IMG2": "Stone Veneer Project",
    },
    "Hardscaping/Retaining Walls/Materials/Wooden Walls/index.html": {
        "TITLE": "Wooden Retaining Walls",
        "HERO_H1": "Builders &amp; Designers of Wooden Retaining Walls",
        "HERO_SUB": "Warm timber walls for informal landscapes, garden beds, and budget-conscious grade changes.",
        "S1_H2": "Wood retaining wall contractors throughout the area",
        "S1_P1": "Wooden retaining walls can provide a softer look than masonry or concrete, especially in gardens, side yards, and casual outdoor spaces.",
        "S1_P2": "They are best considered for shorter walls and projects where the natural appearance of timber fits the site. Proper drainage and material selection are important to help the wall perform well over time.",
        "S2_H2": "Why wooden retaining walls work for the right project",
        "S2_P1": "Timber walls bring a natural look to gardens, beds, and rustic hardscapes when designed for the correct height and exposure.",
        "S2_P2": "Placeholder content — replace this section with your final service copy and project photos.",
        "IMG1": "Wooden Retaining Wall",
        "IMG2": "Wooden Wall Project",
    },
    "Hardscaping/Retaining Walls/Type/Cantilever Walls/index.html": {
        "TITLE": "Cantilever Retaining Walls",
        "HERO_H1": "Builders &amp; Designers of Cantilever Retaining Walls",
        "HERO_SUB": "Efficient structural walls that use a reinforced footing and stem to resist soil pressure.",
        "S1_H2": "Cantilever retaining wall contractors throughout the area",
        "S1_P1": "Cantilever retaining walls are commonly used when the project calls for a stronger engineered wall without excessive material bulk. The wall works with a footing and reinforced stem to hold back soil loads.",
        "S1_P2": "This wall type can be finished in concrete, veneer, or other hardscape materials depending on the appearance needed for the property.",
        "S2_H2": "Why cantilever walls are a dependable choice",
        "S2_P1": "Cantilever walls offer a strong solution for larger grade changes and structural retaining needs when footing design is planned correctly.",
        "S2_P2": "Placeholder content — replace this section with your final service copy and project photos.",
        "IMG1": "Cantilever Retaining Wall",
        "IMG2": "Cantilever Wall Project",
    },
    "Hardscaping/Retaining Walls/Type/Gravity Walls/index.html": {
        "TITLE": "Gravity Retaining Walls",
        "HERO_H1": "Builders &amp; Designers of Gravity Retaining Walls",
        "HERO_SUB": "Mass-based walls that rely on weight, batter, and proper base preparation to hold soil in place.",
        "S1_H2": "Gravity retaining wall contractors throughout the area",
        "S1_P1": "Gravity retaining walls use their own mass to resist pressure from the soil behind them. They are often built from block, stone, gabion baskets, or other heavy wall systems.",
        "S1_P2": "This type works well when the site has room for the correct wall depth and the design benefits from a substantial, grounded appearance.",
        "S2_H2": "Why gravity retaining walls perform reliably",
        "S2_P1": "Gravity walls are useful for low to moderate retaining wall heights and pair well with block, stone, and gabion materials.",
        "S2_P2": "Placeholder content — replace this section with your final service copy and project photos.",
        "IMG1": "Gravity Retaining Wall",
        "IMG2": "Gravity Wall Project",
    },
    "Hardscaping/Retaining Walls/Type/Piling Walls/index.html": {
        "TITLE": "Piling Retaining Walls",
        "HERO_H1": "Builders &amp; Designers of Piling Retaining Walls",
        "HERO_SUB": "Deep-support wall systems for tight sites, difficult slopes, and places where excavation space is limited.",
        "S1_H2": "Piling retaining wall contractors throughout the area",
        "S1_P1": "Piling retaining walls use vertical members driven or drilled into the ground to support the retained soil. They can be useful when space is tight or the site conditions require deeper support.",
        "S1_P2": "The layout depends on soil conditions, wall height, nearby structures, drainage, and the finish desired above grade.",
        "S2_H2": "Why piling walls solve tough site conditions",
        "S2_P1": "Piling walls are useful for tight access, challenging slopes, and sites where a smaller footprint is needed behind the retaining face.",
        "S2_P2": "Placeholder content — replace this section with your final service copy and project photos.",
        "IMG1": "Piling Retaining Wall",
        "IMG2": "Piling Wall Project",
    },
    "Hardscaping/Retaining Walls/Type/Anchored Walls/index.html": {
        "TITLE": "Anchored Retaining Walls",
        "HERO_H1": "Builders &amp; Designers of Anchored Retaining Walls",
        "HERO_SUB": "Reinforced retaining systems that use anchors for added resistance on taller or more demanding walls.",
        "S1_H2": "Anchored retaining wall contractors throughout the area",
        "S1_P1": "Anchored retaining walls add support by tying the wall back into stable soil or rock behind the face. This can improve performance where the wall is tall, loads are significant, or space limits other designs.",
        "S1_P2": "The anchor layout, wall face, drainage, and finish are planned together so the wall is strong and visually compatible with the property.",
        "S2_H2": "Why anchored walls handle demanding loads",
        "S2_P1": "Anchored systems add support for taller or more demanding retaining walls and can be paired with concrete, block, or finished wall faces.",
        "S2_P2": "Placeholder content — replace this section with your final service copy and project photos.",
        "IMG1": "Anchored Retaining Wall",
        "IMG2": "Anchored Wall Project",
    },
}

HEADER_PATTERN = re.compile(r"<header class=\"site-header\">.*?</header>", re.DOTALL)


def render_service(page_data: dict) -> str:
    html = TEMPLATE
    html = html.replace("{{NAV}}", NAV.strip())
    for key, value in page_data.items():
        html = html.replace("{{" + key + "}}", value)
    return html


def update_nav_only(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not HEADER_PATTERN.search(text):
        print(f"skip nav (no header): {path.relative_to(ROOT)}")
        return
    updated = HEADER_PATTERN.sub(NAV.strip(), text, count=1)
    path.write_text(updated, encoding="utf-8")
    print(f"nav updated: {path.relative_to(ROOT)}")


def main() -> None:
    for rel_path, data in SERVICE_PAGES.items():
        out = ROOT / rel_path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_service(data), encoding="utf-8")
        print(f"service page: {rel_path}")

    for html_file in ROOT.rglob("*.html"):
        if html_file.name.startswith("_"):
            continue
        text = html_file.read_text(encoding="utf-8")
        if "submenu--mega" in text:
            update_nav_only(html_file)


if __name__ == "__main__":
    main()
