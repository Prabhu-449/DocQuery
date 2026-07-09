# DocQuery – RAG-Based Document Q&A Assistant

DocQuery is an AI-powered document question-answering assistant that helps users ask questions from uploaded documents and retrieve relevant answers using a Retrieval-Augmented Generation workflow.

This project demonstrates practical skills in Natural Language Processing, document processing, vector search, and applied AI.

---

## Problem Statement

Reading long documents manually takes time. Users often need quick answers from PDFs, notes, reports, or text documents.

DocQuery solves this problem by allowing users to upload a document and ask natural language questions. The system searches the document content and returns relevant answers based on the retrieved information.

---

## Key Features

- Upload and process documents
- Extract text from document content
- Split large text into smaller chunks
- Convert text chunks into vector representations
- Search relevant chunks based on user queries
- Generate retrieval-based answers
- Simple and clean user interface
- Useful for research, study notes, reports, and document analysis

---

## Technologies Used

- Python
- Natural Language Processing
- LangChain
- FAISS Vector Search
- Embeddings
- Streamlit / Web UI
- PDF/Text Processing
- GitHub
- Kaggle

---

## Project Workflow

1. User uploads a document
2. Text is extracted from the document
3. Extracted text is split into smaller chunks
4. Chunks are converted into embeddings
5. Embeddings are stored in a vector database
6. User asks a question
7. The system retrieves the most relevant chunks
8. Answer is generated using the retrieved context

---

## Architecture

```text
Document Upload
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
Vector Storage using FAISS
      ↓
User Query
      ↓
Similarity Search
      ↓
Retrieved Context
      ↓
Answer Generation
