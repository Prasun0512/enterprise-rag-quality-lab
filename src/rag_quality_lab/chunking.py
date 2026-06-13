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
