# DocQuery

# DocuQuery – Intelligent Document Question Answering System

## Overview

DocuQuery is a Retrieval-Augmented Generation (RAG) based AI assistant that enables users to interact with PDF documents using natural language queries. The system retrieves relevant information from uploaded documents and generates accurate, context-aware responses using Large Language Models (LLMs).

This project combines document retrieval, vector embeddings, and generative AI to simplify information extraction from lengthy documents.

---

## Features

- Upload and process PDF documents
- Extract text from documents automatically
- Semantic search using vector embeddings
- Retrieval-Augmented Generation (RAG)
- Context-aware question answering
- Fast document retrieval
- Interactive and user-friendly interface

---

## Problem Statement

Searching for specific information in lengthy documents can be time-consuming and inefficient. DocuQuery addresses this challenge by allowing users to ask questions in natural language and receive precise answers directly from the document content.

---

## Technology Stack

### Programming Language
- Python

### AI & Machine Learning
- LangChain
- Large Language Models (LLMs)
- Sentence Transformers

### Vector Database
- FAISS

### Document Processing
- PyPDF2
- PDFPlumber

### Frontend
- Streamlit

### Backend
- Python

---

## System Workflow

1. User uploads a PDF document.
2. Text is extracted from the document.
3. The text is divided into smaller chunks.
4. Embeddings are generated for each chunk.
5. Embeddings are stored in a vector database.
6. User submits a query.
7. Relevant document chunks are retrieved.
8. Retrieved context is passed to the LLM.
9. The system generates an accurate response.

---

## Project Architecture

Document Upload → Text Extraction → Text Chunking → Embedding Generation → Vector Database → Similarity Search → Context Retrieval → LLM Response Generation

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/DocuQuery.git
cd DocuQuery
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## Applications

- Research paper analysis
- Academic assistance
- Legal document review
- Technical documentation search
- Company policy management
- Knowledge management systems

---

## Future Enhancements

- Multi-document support
- Chat history and memory
- OCR support for scanned PDFs
- Support for DOCX and Excel files
- Document summarization
- Citation and reference generation

---

## Project Outcomes

- Improved document search efficiency
- Reduced manual information retrieval effort
- Enhanced user experience through conversational AI
- Practical implementation of Retrieval-Augmented Generation (RAG)

---

## Author

**Prabhu Shankar**

Data Science & Artificial Intelligence Enthusiast

---

## License

This project is developed for educational and research purposes.
