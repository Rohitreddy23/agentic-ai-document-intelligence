# Agentic AI Document Intelligence Platform

A production-style multi-agent AI platform for document classification, information extraction, summarization, validation, question answering, and workflow automation.

This project demonstrates how agentic AI workflows can automate document-heavy enterprise processes using FastAPI, Python, and LangGraph-style orchestration.

## Problem

Enterprise teams often process large volumes of documents manually. Common tasks include reading documents, classifying them, extracting important fields, validating information, summarizing content, and routing results to downstream users or systems.

Manual document processing can be slow, inconsistent, and difficult to scale.

## Solution

This project uses a modular Agentic AI architecture where different agents handle different responsibilities:

- Document Classification Agent
- Information Extraction Agent
- Summarization Agent
- Validation Agent
- Question Answering Agent
- Workflow Orchestration Layer

## Architecture

```text
Enterprise Documents
        |
        v
Document Ingestion
        |
        v
Preprocessing + Text Cleaning
        |
        v
Agentic Workflow Orchestrator
        |
        +-----------------------------+
        |                             |
        v                             v
Classification Agent          Extraction Agent
        |                             |
        v                             v
Summarization Agent           Validation Agent
        |                             |
        +-------------+---------------+
                      |
                      v
              Final Structured Output
                      |
                      v
                FastAPI Service
```

## Demo

Run locally and open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Tech Stack

- Python
- FastAPI
- LangGraph-style workflow design
- LangChain-compatible service structure
- AWS Bedrock / Gemini / Llama compatible LLM design
- Pydantic
- Docker
- Pytest

## Project Structure

```text
agentic-ai-document-intelligence/
├── app/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── main.py
│   └── schemas.py
├── data/sample_documents/
├── docs/
├── tests/
├── .env.example
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

## Key Features

- Document classification
- Information extraction
- Document summarization
- Output validation
- Question answering over document text
- Modular agent design
- Workflow orchestration layer
- FastAPI endpoints
- Docker-ready structure
- Test-ready project layout

## API Endpoints

### Health Check

```http
GET /health
```

### Analyze Document

```http
POST /api/analyze-document
```

Example request:

```json
{
  "document_text": "This is a sample enterprise policy document...",
  "document_name": "sample_policy_document.txt"
}
```

### Ask Document

```http
POST /api/ask-document
```

Example request:

```json
{
  "document_text": "This is a sample enterprise policy document...",
  "question": "What is this document about?"
}
```

## Getting Started

```bash
git clone https://github.com/Rohitreddy23/agentic-ai-document-intelligence.git
cd agentic-ai-document-intelligence
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Sample Use Cases

- Enterprise document processing
- Policy document analysis
- Compliance document review
- Contract summarization
- Automated information extraction
- Internal workflow automation
- Document Q&A assistant

## Future Enhancements

- Add LangGraph state machine implementation
- Integrate AWS Bedrock, Gemini, or Llama
- Add document upload support
- Add OCR support for PDFs and scanned documents
- Add database persistence
- Add extraction and summarization evaluation metrics
- Add frontend dashboard
- Deploy to AWS or Azure

## Author

**Rohith Reddy Chinthala**  
Big Data Engineer and AI/ML Engineer  
LinkedIn: https://www.linkedin.com/in/rohitreddy23/  
GitHub: https://github.com/Rohitreddy23
