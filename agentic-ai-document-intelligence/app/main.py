from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Agentic AI Document Intelligence Platform",
    description="A FastAPI service for multi-agent document classification, extraction, summarization, validation, and Q&A.",
    version="1.0.0",
)

app.include_router(router, prefix="/api", tags=["Document Intelligence"])


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "agentic-ai-document-intelligence"}
