# PROJECT SCOPE — Global Credit Risk MVP (Banking)

## Goal
Build a *local-first* MVP (Windows) for Banking / Credit Risk:
- Forecast *NPL%* for *10 countries* with a horizon of *1–3 years*
- Provide explainability using evidence (RAG) in later sprints

## Sprint 0 Deliverable (this sprint)
- FastAPI API running locally with *mock endpoints*
- Streamlit UI running locally with *3 pages* calling the API
- Countries configurable via config/countries.json

## Locked decisions (MVP)
- Language: Python
- API: FastAPI
- UI: Streamlit
- Countries list: config file (config/countries.json)
- Forecast model (later): baseline + Holt/Holt-Winters
- RAG (later): FAISS + docstore
- LLM (later): mock first, plug-in later

## Out of scope for Sprint 0
- Datasets ingestion
- Forecast training
- FAISS / embeddings
- Docker / AWS deploy