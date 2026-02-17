# ARCHITECTURE — Global Credit Risk Decision Support (MVP)

## Architectural intent
The system is designed to resemble a production AI/ML service in reduced form:
- explicit API contracts;
- clear separation of responsibilities;
- persistent artifacts for reproducibility;
- evidence-based explainability with citations.

The goal is to avoid “notebook-driven” solutions and instead build a system that can evolve incrementally from local development to containerized and cloud-based execution.

---

## Components

### Streamlit UI
Role:
- provides a minimal but concrete interface for selecting country/horizon,
  ingesting documents, querying evidence, and requesting explanations.

Rationale:
- enables end-to-end validation and demo without investing in a full front-end stack.

### FastAPI (contract and orchestration layer)
Role:
- exposes stable REST endpoints;
- orchestrates domain logic while keeping UI thin.

Domain boundaries:
- /v1/forecast/*: training, evaluation, prediction, artifact persistence;
- /v1/knowledge/*: document ingestion, indexing, retrieval, citations;
- /v1/decision/*: composition of forecast outputs and retrieved evidence.

This separation reduces coupling and allows independent evolution of components.

---

## Domain modules

### Forecast
Responsibilities:
- load normalized time series per country;
- train baseline and Holt/Holt-Winters models;
- evaluate using time-aware backtesting;
- select the preferred approach based on metrics;
- persist models and evaluation metadata;
- generate 1–3 year forecasts.

Rationale:
- baseline enforces a minimum performance reference;
- Holt/Holt-Winters offers interpretability and robustness with limited data;
- trade-off favors transparency and stability over model complexity.

### Knowledge (RAG)
Responsibilities:
- ingest documents (PDF/MD/TXT);
- chunk text and compute embeddings locally;
- index vectors using FAISS and persist the index;
- maintain a docstore with chunk text and metadata for citation;
- retrieve top‑k evidence for a query.

Rationale:
- FAISS provides efficient local similarity search;
- docstore is required for traceability and source attribution.

### Decision (Explain)
Responsibilities:
- combine forecast summary (trend, horizon, model, metrics);
- combine retrieved evidence (chunks and metadata);
- return an explanation with citations.

Generation strategy:
- deterministic/template-based in the MVP to ensure testability;
- optional LLM integration later without altering contracts.

This positions generation as an interchangeable component, not the source of truth.

---

## Persistence model
Local persistence is a core architectural choice:

- data/raw/ and data/processed/: raw and normalized datasets;
- artifacts/: trained models and evaluation metrics;
- vector_store/: FAISS index and docstore (evidence and citations).

Persistence supports reproducibility, debugging, and governance discussions.

---

## End-to-end flow
1) user selects country/horizon in the UI;
2) UI calls forecast training and prediction endpoints;
3) user ingests documents into the knowledge base;
4) user queries evidence with sources;
5) user requests a decision explanation combining forecast and evidence.

---

## Promotion to Docker and AWS
The architecture is compatible with containerization:
- API and UI run as separate processes;
- persistent directories can be mounted as volumes.

Cloud deployment (e.g., AWS EC2) is a promotion step after local validation, not a prerequisite for correctness.