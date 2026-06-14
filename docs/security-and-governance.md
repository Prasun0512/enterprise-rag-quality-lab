# Security and Governance

## Data Safety

- Redact sensitive values before indexing and logging.
- Keep evaluation datasets synthetic or sanitized.
- Store source references and citations without exposing private content.
- Avoid indexing documents outside approved retention and access rules.

## RAG Governance

- Version chunking, embedding model, retrieval parameters, prompts, and evaluation data.
- Track groundedness, citation coverage, answer relevance, and retrieval recall.
- Fail release gates when regression metrics fall below agreed thresholds.
- Route low-confidence or unsupported answers to review.

## Production Controls

- Apply document-level ACL filtering before retrieval.
- Monitor cost, latency, retrieval failures, and no-answer rates.
- Add prompt injection and data exfiltration tests before enabling external content ingestion.
