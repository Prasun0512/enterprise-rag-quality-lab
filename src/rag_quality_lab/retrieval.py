"""Simple lexical retrieval baseline for RAG evaluation."""

from __future__ import annotations

from dataclasses import dataclass

from .chunking import tokenize


@dataclass(frozen=True)
class Document:
    id: str
    title: str
    text: str


@dataclass(frozen=True)
class RetrievalHit:
    id: str
    title: str
    score: float
    text: str


class LexicalRetriever:
    def __init__(self, documents: list[Document]) -> None:
        self.documents = documents
        self._doc_terms = {doc.id: set(tokenize(doc.title + " " + doc.text)) for doc in documents}

    def search(self, query: str, k: int = 3) -> list[RetrievalHit]:
        query_terms = set(tokenize(query))
        if not query_terms:
            return []

        hits: list[RetrievalHit] = []
        for doc in self.documents:
            doc_terms = self._doc_terms[doc.id]
            overlap = query_terms.intersection(doc_terms)
            score = len(overlap) / len(query_terms)
            if score > 0:
                hits.append(RetrievalHit(id=doc.id, title=doc.title, score=score, text=doc.text))

        return sorted(hits, key=lambda hit: (-hit.score, hit.id))[:k]
