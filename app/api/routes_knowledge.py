from fastapi import APIRouter, UploadFile, File
from typing import List, Optional

router = APIRouter()

@router.post("/ingest")
async def ingest(files: List[UploadFile] = File(...), tags: Optional[str] = None):
    return {
        "files_received": [f.filename for f in files],
        "tags": tags,
        "note": "Sprint 0 mock. Sprint 5/6 will implement embeddings + FAISS + docstore."
    }

@router.post("/query")
def query(payload: dict):
    return {
        "answer": "Sprint 0 mock answer (no RAG yet).",
        "sources": [],
        "note": "Sprint 6 will implement retrieval top-k + sources."
    }