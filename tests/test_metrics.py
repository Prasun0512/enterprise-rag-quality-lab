from rag_quality_lab.metrics import (
    citation_coverage,
    grounding_score,
    precision_at_k,
    recall_at_k,
    reciprocal_rank,
)


def test_retrieval_metrics() -> None:
    expected = {"a", "c"}
    retrieved = ["a", "b", "c"]

    assert recall_at_k(expected, retrieved, 3) == 1.0
    assert precision_at_k(expected, retrieved, 3) == 2 / 3
    assert reciprocal_rank(expected, retrieved) == 1.0


def test_grounding_and_citation_metrics() -> None:
    assert citation_coverage({"doc-1", "doc-2"}, {"doc-1", "doc-3"}) == 0.5
    assert grounding_score({"rag", "citation", "unknown"}, {"rag", "citation"}) == 2 / 3
