from rag_quality_lab.retrieval import Document, LexicalRetriever


def test_lexical_retriever_returns_relevant_document() -> None:
    retriever = LexicalRetriever(
        [
            Document(id="rag", title="RAG Quality", text="Recall and precision measure retrieval quality."),
            Document(id="agent", title="Agent Tools", text="Tool access should be governed."),
        ]
    )

    hits = retriever.search("retrieval precision quality", k=1)

    assert hits[0].id == "rag"
