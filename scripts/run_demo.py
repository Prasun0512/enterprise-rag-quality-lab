from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rag_quality_lab.evaluator import evaluate_question
from rag_quality_lab.redaction import redact_pii
from rag_quality_lab.retrieval import Document, LexicalRetriever


def load_documents() -> list[Document]:
    records = json.loads((ROOT / "examples" / "corpus.json").read_text(encoding="utf-8"))
    return [
        Document(id=row["id"], title=row["title"], text=redact_pii(row["text"]))
        for row in records
    ]


def main() -> None:
    retriever = LexicalRetriever(load_documents())
    questions = json.loads((ROOT / "examples" / "questions.json").read_text(encoding="utf-8"))

    for row in questions:
        result = evaluate_question(
            retriever=retriever,
            question=row["question"],
            expected_ids=set(row["expected_ids"]),
        )
        print(f"\nQuestion: {result.question}")
        print(f"Expected: {sorted(result.expected_ids)}")
        print(f"Retrieved: {[hit.id for hit in result.hits]}")
        print(f"Recall@3: {result.recall_at_3:.2f}")
        print(f"Precision@3: {result.precision_at_3:.2f}")
        print(f"MRR: {result.reciprocal_rank:.2f}")
        print(f"Human review: {result.route_to_human_review}")


if __name__ == "__main__":
    main()
