from rag_quality_lab.chunking import chunk_with_metadata, semantic_style_chunks


def test_metadata_chunks_preserve_document_fields() -> None:
    chunks = chunk_with_metadata(
        "Azure OpenAI uses review gates for sensitive workflows.",
        {"doc_id": "policy-1", "tenant": "demo"},
        chunk_size=5,
        overlap=1,
    )

    assert chunks[0]["chunk_id"] == "policy-1-1"
    assert chunks[0]["metadata"] == {"doc_id": "policy-1", "tenant": "demo"}
    assert "azure" in chunks[0]["text"]


def test_semantic_style_chunks_keep_paragraphs_together() -> None:
    text = "RAG systems need citations.\n\nHuman review handles low confidence."

    chunks = semantic_style_chunks(text, max_tokens=10)

    assert chunks == ["RAG systems need citations. Human review handles low confidence."]
