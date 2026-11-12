"""Publish the two authoring files with stable, readable website addresses."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "docs"
PAGES = {
    "企赢-系统原型.html": "index.html",
    "企赢-产品方案与演示.html": "plan.html",
}


def main():
    OUTPUT.mkdir(exist_ok=True)
    for source, destination in PAGES.items():
        html = (ROOT / source).read_text(encoding="utf-8")
        for original, published in PAGES.items():
            html = html.replace(original, published)
        (OUTPUT / destination).write_text(html, encoding="utf-8")
        print(f"Published {source} → {destination}")


if __name__ == "__main__":
    main()
