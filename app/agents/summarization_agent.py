class SummarizationAgent:
    """Generates a concise summary of the document."""

    def summarize(self, document_text: str) -> str:
        clean_text = " ".join(document_text.split())
        if len(clean_text) <= 250:
            return clean_text
        return clean_text[:250] + "..."
