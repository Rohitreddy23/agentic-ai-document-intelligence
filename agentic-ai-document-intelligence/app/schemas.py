from typing import List, Optional
from pydantic import BaseModel, Field


class AnalyzeDocumentRequest(BaseModel):
    document_text: str = Field(..., description="Raw text from the document")
    document_name: Optional[str] = Field(default=None, description="Optional document name")


class ExtractedField(BaseModel):
    field_name: str
    field_value: str
    confidence: float


class AnalyzeDocumentResponse(BaseModel):
    document_name: Optional[str]
    classification: str
    summary: str
    extracted_fields: List[ExtractedField]
    validation_status: str
    validation_notes: str


class AskDocumentRequest(BaseModel):
    document_text: str = Field(..., description="Raw text from the document")
    question: str = Field(..., description="Question to answer using the document")


class AskDocumentResponse(BaseModel):
    question: str
    answer: str
