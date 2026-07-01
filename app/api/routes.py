from fastapi import APIRouter
from app.schemas import AnalyzeDocumentRequest, AnalyzeDocumentResponse, AskDocumentRequest, AskDocumentResponse
from app.services.workflow_orchestrator import DocumentWorkflowOrchestrator
from app.agents.qa_agent import QAAgent

router = APIRouter()

workflow = DocumentWorkflowOrchestrator()
qa_agent = QAAgent()


@router.post("/analyze-document", response_model=AnalyzeDocumentResponse)
def analyze_document(payload: AnalyzeDocumentRequest):
    return workflow.run(document_text=payload.document_text, document_name=payload.document_name)


@router.post("/ask-document", response_model=AskDocumentResponse)
def ask_document(payload: AskDocumentRequest):
    answer = qa_agent.answer_question(payload.document_text, payload.question)
    return AskDocumentResponse(question=payload.question, answer=answer)
