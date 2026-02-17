# Global Credit Risk MVP (Sprint 0)

FastAPI + Streamlit running locally on Windows with mock endpoints.

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
