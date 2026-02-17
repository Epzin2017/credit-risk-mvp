from fastapi import APIRouter

router = APIRouter()

@router.post("/explain")
def explain(payload: dict):
    country = payload.get("country", "Unknown")
    return {
        "summary": f"Sprint 0 mock explanation for {country}.",
        "sources": [],
        "note": "Sprint 7 will combine forecast + RAG evidence with citations."
    }