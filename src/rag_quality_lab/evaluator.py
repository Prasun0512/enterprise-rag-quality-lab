"""End-to-end RAG retrieval evaluation workflow."""

from __future__ import annotations

from dataclasses import dataclass

from .metrics import precision_at_k, recall_at_k, reciprocal_rank
from .retrieval import LexicalRetriever, RetrievalHit


@dataclass(frozen=True)
class EvaluationResult:
    question: str
    expected_ids: set[str]
    hits: list[RetrievalHit]
    recall_at_3: float
    precision_at_3: float
    reciprocal_rank: float
    route_to_human_review: bool


def evaluate_question(
    retriever: LexicalRetriever,
    question: str,
    expected_ids: set[str],
    k: int = 3,
    review_threshold: float = 0.67,
) -> EvaluationResult:
    hits = retriever.search(question, k=k)
    retrieved_ids = [hit.id for hit in hits]
    recall = recall_at_k(expected_ids, retrieved_ids, k)
    precision = precision_at_k(expected_ids, retrieved_ids, k)
    rr = reciprocal_rank(expected_ids, retrieved_ids)

    return EvaluationResult(
        question=question,
        expected_ids=expected_ids,
        hits=hits,
        recall_at_3=recall,
        precision_at_3=precision,
        reciprocal_rank=rr,
        route_to_human_review=recall < review_threshold,
    )
