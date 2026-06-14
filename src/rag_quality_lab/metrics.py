"""Retrieval metrics used by the demo evaluator."""

from __future__ import annotations


def recall_at_k(expected: set[str], retrieved: list[str], k: int) -> float:
    if not expected:
        return 0.0
    return len(expected.intersection(retrieved[:k])) / len(expected)


def precision_at_k(expected: set[str], retrieved: list[str], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if not retrieved:
        return 0.0
    return len(expected.intersection(retrieved[:k])) / min(k, len(retrieved))


def reciprocal_rank(expected: set[str], retrieved: list[str]) -> float:
    for index, doc_id in enumerate(retrieved, start=1):
        if doc_id in expected:
            return 1 / index
    return 0.0


def citation_coverage(answer_citations: set[str], retrieved_ids: set[str]) -> float:
    """Measure how many cited sources are present in retrieved context."""
    if not answer_citations:
        return 0.0
    return len(answer_citations.intersection(retrieved_ids)) / len(answer_citations)


def grounding_score(answer_terms: set[str], context_terms: set[str]) -> float:
    """Estimate whether answer terms are supported by retrieved context terms."""
    if not answer_terms:
        return 0.0
    return len(answer_terms.intersection(context_terms)) / len(answer_terms)
