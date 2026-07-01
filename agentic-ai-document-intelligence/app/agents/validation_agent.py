from app.schemas import ExtractedField


class ValidationAgent:
    """Validates extracted outputs before final response."""

    def validate(self, extracted_fields: list[ExtractedField]) -> tuple[str, str]:
        if not extracted_fields:
            return "failed", "No extracted fields were found."
        return "passed", "Document analysis completed with required extracted fields."
