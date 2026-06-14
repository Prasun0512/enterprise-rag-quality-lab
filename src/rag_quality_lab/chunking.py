"""Text normalization and deterministic chunking."""

from __future__ import annotations

import re

TOKEN_RE = re.compile(r"[a-z0-9]+")


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def chunk_text(text: str, chunk_size: int = 90, overlap: int = 15) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")

    tokens = tokenize(normalize_text(text))
    if not tokens:
        return []

    chunks: list[str] = []
    start = 0
    while start < len(tokens):
        end = min(start + chunk_size, len(tokens))
        chunks.append(" ".join(tokens[start:end]))
        if end == len(tokens):
            break
        start = end - overlap
    return chunks


def chunk_with_metadata(
    text: str,
    metadata: dict[str, str],
    chunk_size: int = 90,
    overlap: int = 15,
) -> list[dict[str, object]]:
    """Create chunks that carry document metadata for filtered retrieval."""
    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
    return [
        {
            "chunk_id": f"{metadata.get('doc_id', 'doc')}-{index}",
            "text": chunk,
            "metadata": dict(metadata),
        }
        for index, chunk in enumerate(chunks, start=1)
    ]


def semantic_style_chunks(text: str, max_tokens: int = 90) -> list[str]:
    """Group paragraphs into chunks without splitting short sections.

    This is dependency-light and deterministic. It is not a true embedding-based
    semantic splitter, but it mirrors the production design goal: preserve
    coherent sections before applying a token budget.
    """
    if max_tokens <= 0:
        raise ValueError("max_tokens must be positive")

    paragraphs = [normalize_text(part) for part in re.split(r"\n\s*\n", text) if part.strip()]
    if not paragraphs:
        return []

    chunks: list[str] = []
    current: list[str] = []
    current_tokens = 0

    for paragraph in paragraphs:
        token_count = len(tokenize(paragraph))
        if current and current_tokens + token_count > max_tokens:
            chunks.append(" ".join(current))
            current = [paragraph]
            current_tokens = token_count
        else:
            current.append(paragraph)
            current_tokens += token_count

    if current:
        chunks.append(" ".join(current))

    return chunks
