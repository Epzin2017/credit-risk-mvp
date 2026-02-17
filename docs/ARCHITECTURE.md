# ARCHITECTURE — Sprint 0 (Global Credit Risk MVP)

## Objective
Sprint 0 delivers a *running skeleton*:
- FastAPI API with mock endpoints
- Streamlit UI with 3 pages calling the API
- Countries list configurable via config/countries.json

> No forecasting model, no FAISS, no datasets yet.

---

## Components
### 1) API (FastAPI)
- Runs at: http://localhost:8000
- Endpoints:
  - GET /health
  - POST /v1/forecast/train (mock)
  - POST /v1/forecast/predict (mock)
  - POST /v1/knowledge/ingest (mock)
  - POST /v1/knowledge/query (mock)
  - POST /v1/decision/explain (mock)
- Swagger:
  - http://localhost:8000/docs

### 2) UI (Streamlit)
- Runs at: http://localhost:8501
- Pages:
  - Forecast
  - Knowledge
  - Explain
- Calls the API endpoints above (mock).

### 3) Configuration
- Countries list:
  - config/countries.json

---