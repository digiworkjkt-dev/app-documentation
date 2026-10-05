#!/usr/bin/env python3
"""Structural validation only; no conformity assessment or visual print QA."""
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


class TemplateParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.external_resources = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag in {"script", "img", "link", "iframe"}:
            for field in ("src", "href"):
                if attrs.get(field, "").startswith(("http:", "https:", "//")):
                    self.external_resources.append(attrs[field])


def validate():
    main = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert main.startswith("---\n"), "Missing frontmatter"
    front = main.split("---", 2)[1]
    name = re.search(r"^name: (.+)$", front, re.M)
    description = re.search(r"^description: (.+)$", front, re.M)
    assert name and re.fullmatch(r"[a-z0-9-]{1,64}", name[1])
    assert description and len(description[1]) <= 1024
    assert len(main.splitlines()) < 500
    for file in ROOT.rglob("*.md"):
        text = file.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            assert (file.parent / target.split("#", 1)[0]).is_file(), (file, target)
        headings = re.findall(r"^## .+$", text, re.M)
        assert len(headings) == len(set(headings)), f"Duplicate headings: {file}"

    html = (ROOT / "assets/report-a4.html").read_text(encoding="utf-8")
    parser = TemplateParser()
    parser.feed(html)
    assert len(parser.ids) == len(set(parser.ids)), "Duplicate HTML IDs"
    for href in parser.links:
        if href.startswith("#"):
            assert href[1:] in parser.ids, f"Missing anchor: {href}"
    assert not parser.external_resources, "External rendering dependencies"
    for required in (
        "size: A4 portrait", "margin: 3cm", "Cambria", "font-size: 12pt",
        "@media print", "table-header-group", "break-before: page",
        "lang=\"id\"", "charset=\"utf-8\"",
    ):
        assert required in html, f"Missing print requirement: {required}"
    assert re.search(r'\.report\s*\{[^}]*padding:\s*0', html), "Double print margin risk"
    assert "position: fixed" not in html, "Unverified repeating footer"
    assert "html-print.md" in main and "report-a4.html" in main
    assert "app-documentation/laporan-dokumentasi-aplikasi.html" in main
    assert "Seluruh output dokumen disimpan di folder" in main
    print("PASS: metadata, links, headings, anchors, self-contained template and print rules.")
    print("Not checked: visual pagination, font availability, SNI conformity or competence.")


if __name__ == "__main__":
    validate()
