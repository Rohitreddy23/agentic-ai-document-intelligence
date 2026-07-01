class ClassificationAgent:
    """Classifies enterprise documents into broad categories."""

    def classify(self, document_text: str) -> str:
        text = document_text.lower()

        if "policy" in text or "procedure" in text:
            return "Policy Document"
        if "contract" in text or "agreement" in text:
            return "Contract Document"
        if "compliance" in text or "audit" in text:
            return "Compliance Document"
        if "report" in text or "analysis" in text:
            return "Business Report"

        return "General Enterprise Document"
