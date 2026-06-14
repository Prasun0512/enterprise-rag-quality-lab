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

## Architecture Decisions and Tradeoffs

- **Decision:** Keep a deterministic local retrieval baseline before adding
  managed vector databases or LLM calls.
- **Tradeoff:** Lexical retrieval is less powerful than embeddings, but it is
  explainable, reproducible, and useful as a regression baseline.
- **Expected scale:** Designed as a quality-lab pattern for evaluating retrieval
  changes before applying them to larger enterprise document collections.
- **Cost strategy:** Measure retrieval quality before adding rerankers or premium
  generation models; cache embeddings when production backends are added.
- **Security strategy:** Mask PII before indexing where required and enforce
  tenant/role metadata filters in production extensions.
- **Operational strategy:** Track recall@k, precision@k, reciprocal rank,
  citation support, no-answer rate, and review routing.
- **Lessons learned:** RAG quality is an evaluation discipline, not only a vector
  database implementation.

## Quick Start

```bash
python scripts/run_demo.py
python -m pytest
docker compose up --build
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

## Engineering Maturity

- Dockerfile and `docker-compose.yml` with a local PostgreSQL service placeholder
- GitHub Actions workflow for tests
- Architecture overview in `docs/architecture.md`
- Production readiness notes in `docs/production-readiness.md`
- Security and governance guidance in `docs/security-and-governance.md`
- `.env.example` for Azure AI Search, PostgreSQL, and vector backend configuration
- Production readiness notes in `docs/production-readiness.md`
- Security, monitoring, cost, scalability, and feedback-loop considerations documented
