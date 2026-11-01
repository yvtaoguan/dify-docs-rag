from __future__ import annotations

import json
import re
from pathlib import Path

CLEAN_DIR = Path("data/clean")
CHUNKED_DIR = Path("data/chunked")
JSONL_PATH = Path("data/chunks.jsonl")
SOURCE_BASE = "https://docs.dify.ai/en/cloud/use-dify"
SEPARATOR = "<<<CHUNK>>>"
MAX_CHARS = 1000
MIN_SECTION_CHARS = 30


def split_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    lines = text.splitlines()
    doc_title = ""
    for line in lines:
        if line.startswith("# "):
            doc_title = line[2:].strip()
            break

    h2_indices = [i for i, line in enumerate(lines) if line.startswith("## ")]
    if not h2_indices:
        body = "\n".join(line for line in lines if not line.startswith("# ")).strip()
        return doc_title, [(doc_title, body)]

    sections: list[tuple[str, str]] = []

    intro_body = "\n".join(
        line for line in lines[: h2_indices[0]] if not line.startswith("# ")
    ).strip()
    if len(intro_body) >= MIN_SECTION_CHARS:
        sections.append(("Overview", intro_body))

    for idx, start in enumerate(h2_indices):
        end = h2_indices[idx + 1] if idx + 1 < len(h2_indices) else len(lines)
        section_title = lines[start][3:].strip()
        body = "\n".join(lines[start + 1 : end]).strip()
        if len(body) >= MIN_SECTION_CHARS:
            sections.append((section_title, body))

    return doc_title, sections


def split_long_text(text: str, max_chars: int = MAX_CHARS) -> list[str]:
    paragraphs = re.split(r"\n{2,}", text)
    chunks: list[str] = []
    current = ""

    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        candidate = f"{current}\n\n{paragraph}".strip() if current else paragraph
        if len(candidate) <= max_chars:
            current = candidate
            continue

        if current:
            chunks.append(current)
            current = ""

        while len(paragraph) > max_chars:
            chunks.append(paragraph[:max_chars].strip())
            paragraph = paragraph[max_chars:].strip()

        current = paragraph

    if current:
        chunks.append(current)

    return chunks or [text.strip()]


def main() -> None:
    CHUNKED_DIR.mkdir(parents=True, exist_ok=True)
    all_chunks = []
    files = sorted(CLEAN_DIR.rglob("*.md"))

    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(CLEAN_DIR)
        doc_id = rel.with_suffix("").as_posix().replace("/", "__")
        source_url = f"{SOURCE_BASE}/{rel.with_suffix('').as_posix()}"

        doc_title, sections = split_sections(text)
        doc_title = doc_title or doc_id
        chunks_for_doc = []

        for section_title, body in sections:
            parts = split_long_text(body)
            for i, part in enumerate(parts, 1):
                if section_title == doc_title:
                    heading = f"# {doc_title}"
                else:
                    heading = f"# {doc_title}\n## {section_title}"
                if len(parts) > 1:
                    heading += f" (part {i}/{len(parts)})"

                chunk_text = f"{heading}\nSource: {source_url}\n\n{part.strip()}"
                chunks_for_doc.append({
                    "chunk_id": f"{doc_id}__{len(chunks_for_doc) + 1:03d}",
                    "doc_id": doc_id,
                    "title": doc_title,
                    "section": section_title,
                    "source_url": source_url,
                    "char_count": len(chunk_text),
                    "text": chunk_text,
                })

        if not chunks_for_doc:
            continue

        out_path = CHUNKED_DIR / f"{doc_id}.md"
        out_path.write_text(
            f"\n\n{SEPARATOR}\n\n".join(c["text"] for c in chunks_for_doc) + "\n",
            encoding="utf-8",
        )
        all_chunks.extend(chunks_for_doc)

    JSONL_PATH.parent.mkdir(parents=True, exist_ok=True)
    with JSONL_PATH.open("w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print(f"docs: {len(files)}")
    print(f"chunks: {len(all_chunks)}")
    print(f"chunked docs: {CHUNKED_DIR}")
    print(f"jsonl: {JSONL_PATH}")


if __name__ == "__main__":
    main()