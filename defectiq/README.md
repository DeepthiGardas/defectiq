# DefectIQ - Defect & Vulnerability Intelligence Platform

A production-style GenAI / Agentic AI project built on **synthetic data** with mock services
(no real client data). Modules:

| Module | Description |
|---|---|
| A. DoD File Agent | LangGraph workflow: ZIP/Excel processing, filename normalization, exception triage |
| B. Vulnerability Reconciliation | Multi-source LangGraph agent, 15-day SLA checks, human approval |
| C. Defect Classifier | Structured-output LLM classification with evaluation set |
| D. Document RAG | Qdrant + FastAPI conversational search with citations |

**Principle:** deterministic code for facts and rules; LLMs only for judgment and summarization.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # add your API key
docker compose up -d             # postgres + qdrant
uvicorn app.main:app --reload    # http://localhost:8000/docs
pytest
```

## Structure
See `docs/PROGRESS.md` for the roadmap and status.
