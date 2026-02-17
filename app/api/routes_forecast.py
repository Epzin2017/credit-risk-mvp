from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()

class TrainRequest(BaseModel):
    country: str = Field(..., examples=["Brazil"])
    horizon_years: int = Field(3, ge=1, le=3)

class PredictRequest(BaseModel):
    country: str = Field(..., examples=["Brazil"])
    horizon_years: int = Field(3, ge=1, le=3)

@router.post("/train")
def train(req: TrainRequest):
    return {
        "country": req.country,
        "horizon_years": req.horizon_years,
        "model_selected": "mock",
        "metrics": {"mape": None, "wape": None},
        "note": "Sprint 0 mock. Sprint 2 will implement baseline + Holt/Holt-Winters."
    }

@router.post("/predict")
def predict(req: PredictRequest):
    return {
        "country": req.country,
        "horizon_years": req.horizon_years,
        "forecast": [],
        "note": "Sprint 0 mock. Sprint 2 will return years + predicted NPL%."
    }