# Architecture Notes

## Goal

This project demonstrates a modular agentic AI architecture for enterprise document intelligence.

## Components

### Document Ingestion
Receives raw document text through an API request. In production, this could read from PDFs, SharePoint, S3, Azure Blob Storage, or enterprise document systems.

### Classification Agent
Classifies documents into categories such as policy, compliance, contract, report, or general document.

### Extraction Agent
Extracts structured information such as entities, dates, departments, obligations, decisions, and action items.

### Summarization Agent
Generates a concise summary of the document.

### Validation Agent
Validates whether extracted outputs are complete and consistent.

### Question Answering Agent
Answers user questions over document text.

### Workflow Orchestrator
Coordinates agent execution and returns a final structured response.

## Why Agentic AI?

Agentic AI is useful when a task has multiple reasoning steps, decision points, tool calls, or specialized responsibilities. Instead of one large prompt doing everything, this architecture separates responsibilities across modular agents.
