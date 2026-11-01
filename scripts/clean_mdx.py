from __future__ import annotations

import csv
import re
import textwrap
from pathlib import Path

RAW_DIR = Path("data/raw")
CLEAN_DIR = Path("data/clean")
META_PATH = Path("data/metadata.csv")
SOURCE_BASE = "https://docs.dify.ai/en/cloud/use-dify"
LICENSE = "CC BY 4.0"
SNAPSHOT = "2026-10-31"


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    raw_fm, body = parts[1], parts[2]
    meta: dict[str, str] = {}
    for line in raw_fm.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, body.lstrip("\n")


def protect_code_blocks(text: str) -> tuple[str, list[str]]:
    blocks: list[str] = []
    pattern = re.compile(r"```.*?```", re.S)

    def repl(match: re.Match[str]) -> str:
        blocks.append(match.group(0))
        return f"@@CODEBLOCK{len(blocks) - 1}@@"

    return pattern.sub(repl, text), blocks


def restore_code_blocks(text: str, blocks: list[str]) -> str:
    for i, block in enumerate(blocks):
        text = text.replace(f"@@CODEBLOCK{i}@@", block)
    return text


def clean_mdx(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(("import ", "export ")):
            continue
        lines.append(line)
    text = "\n".join(lines)

    text = re.sub(r"\{/\*.*?\*/\}", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)

    text, code_blocks = protect_code_blocks(text)

    # Tabs, allowing extra attributes
    def tab_repl(match: re.Match[str]) -> str:
        title = match.group(1)
        content = textwrap.dedent(match.group(2)).strip()
        return f"\n### {title}\n\n{content}\n"

    text = re.sub(
        r'<Tab\b[^>]*\btitle="([^"]+)"[^>]*>(.*?)</Tab>',
        tab_repl,
        text,
        flags=re.S,
    )
    text = re.sub(r"</?Tabs>", "", text)

    # Accordion / Card / Step / Expandable, allowing extra attributes
    for tag in ("Accordion", "Card", "Step", "Expandable"):
        pattern = re.compile(
            rf'<{tag}\b[^>]*\btitle="([^"]+)"[^>]*>(.*?)</{tag}>',
            re.S,
        )

        def repl(match: re.Match[str]) -> str:
            title = match.group(1)
            content = textwrap.dedent(match.group(2)).strip()
            return f"\n### {title}\n\n{content}\n"

        text = pattern.sub(repl, text)

    # Frame: keep caption, regardless of other attributes
    def frame_repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        caption = re.search(r'caption="([^"]*)"', tag)
        return f"\n> Image: {caption.group(1)}\n" if caption else "\n"

    text = re.sub(r"<Frame\b[^>]*>", frame_repl, text)
    text = re.sub(r"</Frame>", "", text)

    # Remove images
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"<img\b[^>]*>", "", text, flags=re.I)

    # Tip / Info / Warning / Note
    for tag, label in (("Tip", "Tip"), ("Info", "Info"), ("Warning", "Warning"), ("Note", "Note")):
        pattern = re.compile(rf"<{tag}>\s*(.*?)\s*</{tag}>", re.S)

        def repl(match: re.Match[str], label: str = label) -> str:
            inner = textwrap.dedent(match.group(1)).strip()
            quoted = "\n".join(
                "> " + line if line.strip() else ">" for line in inner.splitlines()
            )
            return f"> **{label}**\n>\n{quoted}"

        text = pattern.sub(repl, text)

    # Remaining HTML/JSX tags
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</?[A-Za-z][^>]*>", "", text)

    # Directive blocks
    text = re.sub(r":::(?:tip|note|info|warning)\s*\n(.*?)\n:::", r"\1", text, flags=re.S)

    # Relative links -> absolute
    text = re.sub(r"\]\(/en/", "](https://docs.dify.ai/en/", text)

    # Whitespace
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    text = restore_code_blocks(text, code_blocks)
    return text.strip() + "\n"


def main() -> None:
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    files = sorted(RAW_DIR.rglob("*.mdx"))

    for path in files:
        raw = path.read_text(encoding="utf-8")
        meta, body = split_frontmatter(raw)
        title = meta.get("title") or path.stem.replace("-", " ").title()
        body = clean_mdx(body)

        if not re.search(r"^#\s+", body, re.M):
            body = f"# {title}\n\n{body}"

        rel = path.relative_to(RAW_DIR)
        out_path = CLEAN_DIR / rel.with_suffix(".md")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(body, encoding="utf-8")

        rel_no_ext = rel.with_suffix("").as_posix()
        source_url = f"{SOURCE_BASE}/{rel_no_ext}"
        headings = re.findall(r"^(#{1,6})\s+(.+)$", body, re.M)

        rows.append({
            "doc_id": rel_no_ext.replace("/", "__"),
            "title": title,
            "description": meta.get("description", ""),
            "tag": meta.get("tag", ""),
            "section": rel.parts[0] if rel.parts else "",
            "source_path": f"data/raw/{rel.as_posix()}",
            "clean_path": f"data/clean/{rel.with_suffix('.md').as_posix()}",
            "source_url": source_url,
            "license": LICENSE,
            "snapshot": SNAPSHOT,
            "char_count": len(body),
            "heading_count": len(headings),
        })

    META_PATH.parent.mkdir(parents=True, exist_ok=True)
    with META_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["doc_id"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"cleaned {len(rows)} files")
    print(f"output: {CLEAN_DIR}")
    print(f"metadata: {META_PATH}")


if __name__ == "__main__":
    main()