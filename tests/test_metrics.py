from rag_quality_lab.metrics import precision_at_k, recall_at_k, reciprocal_rank


def test_retrieval_metrics() -> None:
    expected = {"a", "c"}
    retrieved = ["a", "b", "c"]

    assert recall_at_k(expected, retrieved, 3) == 1.0
    assert precision_at_k(expected, retrieved, 3) == 2 / 3
    assert reciprocal_rank(expected, retrieved) == 1.0
