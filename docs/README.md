# Global Credit Risk Decision Support (MVP)

A local-first decision support system for global credit risk.  
The MVP forecasts the evolution of non-performing loans (NPL%) for 10 countries over a 1–3 year horizon and provides evidence-backed explanations based on a document knowledge base (RAG), including source citations.

The system is intentionally developed locally to stabilize behavior, validate assumptions, and ensure reproducibility before any containerization or cloud deployment.

---

## Context and problem

In regulated environments such as banking and risk management, forecasts are rarely accepted in isolation. Decision-makers typically require:

- a forward-looking risk estimate,
- a clear evaluation of forecast quality against simple baselines,
- and a justification grounded in documented evidence (definitions, policies, reports, methodologies).

This MVP addresses that gap by treating forecasting and explanation as a single system rather than disconnected steps. Quantitative projections and qualitative context are produced together, through explicit contracts and persistent artifacts.

---

## What the MVP delivers (end state)

### Forecasting (per country)
- loads and normalizes historical NPL% time series;
- trains a simple baseline and a Holt / Holt-Winters model;
- evaluates both using time-aware backtesting;
- produces a 1–3 year forecast;
- persists model artifacts and evaluation metrics for reproducibility.

### Knowledge base (RAG)
- ingests PDF/MD/TXT documents;
- chunks and embeds text locally;
- indexes embeddings using FAISS and persists the index;
- stores chunk text and metadata in a local docstore to support citations;
- answers queries by returning top‑k evidence chunks with source metadata.

### Decision explanation
- combines a forecast summary with retrieved evidence;
- returns an explanation with explicit citations;
- starts with deterministic/template-based generation, allowing an LLM to be plugged in later without changing system contracts.

---

## High-level architecture

- Streamlit provides a minimal UI for selecting country/horizon, ingesting documents, and requesting explanations.
- FastAPI exposes stable REST contracts and orchestrates domain logic.
- Domain modules are split into forecast, knowledge, and decision responsibilities.
- All relevant artifacts are persisted locally to ensure reproducibility.

Architectural rationale and trade-offs are documented in docs/ARCHITECTURE.md.  
Product boundaries and constraints are defined in docs/PROJECT_SCOPE.md.

---

## Technology stack

- Python 3.11+
- FastAPI + Uvicorn
- Streamlit
- Forecasting: pandas / numpy + statsmodels (Holt / Holt-Winters) with a baseline comparator
- RAG: sentence-transformers (local embeddings), FAISS, JSON-based docstore
- Local persistence: data/, artifacts/, vector_store/

Containerization (Docker) and AWS deployment are planned as a promotion step once local behavior is stable.


## Run (PowerShell)

### Install
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt


Terminal 1 (API)

 
uvicorn app.main:app --reload --port 8000
 

Terminal 2 (UI)

 
.\.venv\Scripts\Activate.ps1
streamlit run ui\app.py
 

API docs: http://localhost:8000/docs

UI: http://localhost:8501
