# Enterprise RAG Quality Lab

Runnable, dependency-light lab for demonstrating production-minded RAG quality
patterns: PII redaction, chunking, retrieval, citation-aware answer packaging,
and measurable retrieval evaluation.

This project is designed as a clean portfolio artifact for senior AI/ML and
GenAI architecture discussions. It does not call external LLM APIs by default,
so it can run locally and safely.

## What It Demonstrates

- Text normalization and PII masking before indexing
- Deterministic chunking for retrieval pipelines
- Simple lexical retrieval baseline for explainable evaluation
- Recall@k, precision@k, and reciprocal-rank metrics
- Confidence-based review routing for low-quality retrieval
- Reproducible demo data and tests

## Quick Start

```bash
python scripts/run_demo.py
python -m pytest
```

## Example Output

The demo evaluates questions against a small enterprise AI knowledge corpus and
prints retrieved document IDs, quality metrics, and whether the answer should be
routed to human review.

## Repository Structure

```text
src/rag_quality_lab/
  chunking.py        Text normalization and chunking
  redaction.py       Email and phone masking helpers
  retrieval.py       Simple lexical retriever
  metrics.py         RAG retrieval metrics
  evaluator.py       End-to-end evaluation workflow
examples/
  corpus.json        Demo knowledge records
  questions.json     Golden retrieval questions
scripts/
  run_demo.py        Local demo runner
tests/
  test_*.py          Unit tests for core logic
```

## Production Extensions

- Replace lexical retrieval with Azure AI Search, FAISS, Pinecone, or pgvector
- Add embedding model experiments and retrieval benchmark reports
- Add LLM answer generation with citation validation
- Add prompt registry and evaluation dashboards
- Add PHI/PII policies before ingestion and generation
