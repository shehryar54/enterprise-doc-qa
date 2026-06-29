## Enterprise Document Q&A System

A production-style backend system that lets users upload documents (PDF, CSV) 
and query them using natural language — powered by a RAG pipeline running 
entirely on local LLMs.

### How it works
1. Upload any document (PDF or CSV)
2. System chunks and embeds the content into a vector database (ChromaDB)
3. Ask a question in plain English
4. System retrieves relevant chunks and generates an accurate answer via LLaMA 3.2 (Ollama)

### Tech Stack
- **FastAPI** — REST API backend
- **LangChain** — RAG pipeline orchestration
- **ChromaDB** — Vector database for semantic search
- **Ollama + LLaMA 3.2** — Local LLM inference (no OpenAI dependency)
- **Python** — Core language

### Use Cases
- Query company HR policies
- Ask questions about financial reports
- Extract insights from ERP/SAP CSV exports
