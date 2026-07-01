from app.schemas import ExtractedField


class ExtractionAgent:
    """Extracts structured fields from document text."""

    def extract(self, document_text: str) -> list[ExtractedField]:
        words = document_text.split()

        return [
            ExtractedField(
                field_name="document_length_words",
                field_value=str(len(words)),
                confidence=0.99,
            ),
            ExtractedField(
                field_name="contains_policy_keyword",
                field_value=str("policy" in document_text.lower()),
                confidence=0.90,
            ),
        ]
