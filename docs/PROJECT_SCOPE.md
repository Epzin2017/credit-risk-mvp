# PROJECT SCOPE — Global Credit Risk Decision Support (MVP)

## Product purpose
This project simulates a realistic banking risk scenario: producing a short-term (1–3 year) view of credit risk across countries and supporting interpretation with traceable documentary evidence.

The MVP is designed as a small but production-minded system, emphasizing reproducibility, explicit contracts, and controlled scope.

## Target users
- Credit risk and portfolio analysts monitoring asset quality by geography;
- Planning stakeholders who require both a projected number and a defensible narrative;
- Review and governance participants who require traceability of assumptions and sources.

## Definition of done (MVP)
The MVP is considered complete when it can:
1) load and normalize NPL% time series for 10 configured countries;
2) train and evaluate a baseline versus Holt/Holt-Winters using time-aware backtesting;
3) produce a 1–3 year forecast and persist artifacts and metrics locally;
4) ingest documents and enable semantic retrieval with source metadata;
5) generate an explanation that combines forecast outputs with cited evidence.

## In scope
- Local-first execution on Windows;
- FastAPI contracts separated by domain:
  - forecast (training, prediction, metrics, persistence);
  - knowledge (ingestion, indexing, retrieval, citations);
  - decision (composition of forecast + evidence).
- Streamlit UI for concrete demonstration and validation;
- Forecasting approach:
  - mandatory baseline comparator;
  - Holt / Holt-Winters as the primary model;
  - explicit temporal validation and metrics.
- Knowledge management (RAG):
  - document ingestion (PDF/MD/TXT);
  - chunking and local embeddings;
  - FAISS index persisted to disk;
  - docstore persisted for traceability and citations.
- Explanation:
  - deterministic/template-based generation in the MVP;
  - optional LLM integration later without changing API contracts.

## Out of scope (intentional)
To keep the MVP controlled and deliverable, the following are excluded:
- authentication, authorization, and multi-tenancy;
- full production hardening (rate limiting, monitoring stacks, SLOs);
- streaming ingestion or distributed pipelines;
- deep learning forecasting models and heavy hyperparameter tuning;
- full product-grade front-end (SPA);
- cloud deployment as a requirement.

## Non-goals
- Not a replacement for human risk judgment;
- Not a regulatory stress-testing framework;
- Not a crisis prediction system;
- Not a generic document chatbot.

## Constraints and assumptions
- Annual data frequency is assumed in the MVP, targeting macro-level planning;
- Forecast horizon is limited to 1–3 years due to data availability;
- Explanations must always include citations to avoid ungrounded narratives.

## Post-MVP promotion
Docker and AWS are intentionally deferred until the system’s local behavior is stable.  
The architecture and contracts are designed to allow containerization and cloud deployment without structural refactoring.