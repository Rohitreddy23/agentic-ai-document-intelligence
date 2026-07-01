from app.agents.classifier_agent import ClassificationAgent
from app.agents.extraction_agent import ExtractionAgent
from app.agents.summarization_agent import SummarizationAgent
from app.agents.validation_agent import ValidationAgent
from app.schemas import AnalyzeDocumentResponse


class DocumentWorkflowOrchestrator:
    """Coordinates document intelligence agents."""

    def __init__(self):
        self.classifier = ClassificationAgent()
        self.extractor = ExtractionAgent()
        self.summarizer = SummarizationAgent()
        self.validator = ValidationAgent()

    def run(self, document_text: str, document_name: str | None = None) -> AnalyzeDocumentResponse:
        classification = self.classifier.classify(document_text)
        extracted_fields = self.extractor.extract(document_text)
        summary = self.summarizer.summarize(document_text)
        validation_status, validation_notes = self.validator.validate(extracted_fields)

        return AnalyzeDocumentResponse(
            document_name=document_name,
            classification=classification,
            summary=summary,
            extracted_fields=extracted_fields,
            validation_status=validation_status,
            validation_notes=validation_notes,
        )
