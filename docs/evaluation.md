# Evaluation Strategy

RAG quality should be measured before adding expensive models or production vector databases.

## Metrics

- `recall@k`: whether expected supporting documents are retrieved.
- `precision@k`: how much retrieved context is relevant.
- `MRR`: how early the first relevant result appears.
- Grounding score: whether answer claims are supported by retrieved context.
- Citation coverage: whether final answers cite relevant source chunks.
- Review routing: whether weak retrieval is surfaced for human review.

## Local Checks

```bash
python scripts/run_demo.py
python -m pytest
```

## Quality Gates

- Retrieval regressions should block prompt or index changes.
- No-answer behavior should be preferred over unsupported answers.
- Sensitive content must be redacted before indexing when required.
- Low confidence should route to review rather than fabricate certainty.

## Future Improvements

- Add embedding and reranking benchmark modes.
- Generate Markdown evaluation reports from sample questions.
- Add prompt-injection and source-quality test cases.
