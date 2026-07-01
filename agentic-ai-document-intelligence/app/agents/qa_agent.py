class QAAgent:
    """Answers questions using document text."""

    def answer_question(self, document_text: str, question: str) -> str:
        preview = " ".join(document_text.split())[:300]
        return (
            "This is a sample document-grounded answer. "
            "In production, this agent would use an LLM to answer using the supplied document context. "
            f"Question: {question}. Document preview: {preview}"
        )
