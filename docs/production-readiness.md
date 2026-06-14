# Production Readiness

## Deployment

- Run ingestion, embedding, retrieval API, and evaluation jobs as separate services.
- Use Azure AI Search for hybrid retrieval and PostgreSQL/pgvector for portable vector-store experiments.
- Keep benchmark datasets versioned with prompt and chunking configuration.

## Security

- Apply PII masking before indexing where policy requires.
- Enforce tenant and role filters at retrieval time.
- Store credentials in managed secrets, not environment files.

## Monitoring

- Track recall@k, precision@k, reciprocal rank, citation support, latency, and review rate.
- Alert on retrieval-quality regressions after index or prompt changes.

## Cost Optimization

- Cache embeddings by content hash.
- Batch ingestion and embedding jobs.
- Use lexical or hybrid baselines before adding costly reranking.

## Scalability

- Partition indexes by tenant, domain, or data sensitivity.
- Use async ingestion for large document backlogs.
- Add feedback loops from human review into evaluation datasets.
