# Security and Privacy

This document complements `docs/security-and-governance.md`.

## RAG Data Protection

- Redact sensitive data before indexing or logging.
- Use sanitized corpora for public examples.
- Do not commit private documents, credentials, internal URLs, or proprietary prompts.
- Preserve citations without exposing private source text.

## Production Controls

- Enforce document-level ACLs before retrieval.
- Add tenant and role metadata filters.
- Monitor prompt injection, data exfiltration attempts, no-answer rate, and retrieval failures.
- Track model, embedding, prompt, and index versions.
