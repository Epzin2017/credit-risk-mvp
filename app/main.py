from fastapi import FastAPI
from app.api.routes_forecast import router as forecast_router
from app.api.routes_knowledge import router as knowledge_router
from app.api.routes_decision import router as decision_router

app = FastAPI(
    title="Global Credit Risk MVP (Sprint 0)",
    version="0.1.0",
    description="Sprint 0: API skeleton with mock endpoints."
)

app.include_router(forecast_router, prefix="/v1/forecast", tags=["forecast"])
app.include_router(knowledge_router, prefix="/v1/knowledge", tags=["knowledge"])
app.include_router(decision_router, prefix="/v1/decision", tags=["decision"])

@app.get("/health")
def health():
    return {"status": "ok"}