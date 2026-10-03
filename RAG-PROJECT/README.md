# Enterprise Knowledge Intelligence Platform

## Problem Statement
As per current confluence pages it's difficult to find the relevant info from 1000's of documents. 100's of pdf's
## Goals
Retrieve relevant info from enterprise documents
generate answers ground to Retrieved context
Low hallucinations
provide source citations for the answers
follow the gaurdrails
Support document update
## Functional Requirements
User can input query and get the top 2 relevant document based info
User can update documents
User can delete documents
User can view the citations
## Non-Functional Requirements
highly availability
reliability
security
observability
## High-Level Architecture
Ingestion :-
    Document -> parser (parse diff docs) -> chunking -> metadata extraction -> embedding -> vector db
Retrival :-
    query -> query embedding -> retriver -> context -> LLM -> answers + citations
## Request Flow
User
 ↓
FastAPI
 ↓
Query validation
 ↓
Query embedding
 ↓
Vector search
 ↓
Top N chunks
 ↓
Reranking
 ↓
Top K context
 ↓
Prompt construction
 ↓
LLM
 ↓
Answer
 ↓
Citations
 ↓
User
## Document Ingestion Flow
PDF
 ↓
Document parser
 ↓
Extract text
 ↓
Clean text
 ↓
Chunk
 ↓
Generate metadata
 ↓
Generate embeddings
 ↓
Store chunks
 ↓
Store embeddings
## Technology Choices
Python
FastAPI
LLM (Ollama or Groq)
Streamlit or CopilotKit
PostgreSQL + pgvector
## Initial Limitations
- Only local document ingestion
- No authentication
- No multi-tenancy
- No document ACL
- No hybrid retrieval
- No reranking
- No distributed processing
- No HA deployment
## Future Improvements