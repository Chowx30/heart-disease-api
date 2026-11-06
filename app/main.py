import json
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI

from app.schemas import HeartData, Prediction

model_dir = Path(__file__).resolve().parent.parent / "model"
model = joblib.load(model_dir / "heart_model.joblib")
model_info = json.loads((model_dir / "info.json").read_text())

app = FastAPI(title="Heart Disease Prediction API", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/info")
def info():
    return model_info


@app.post("/predict", response_model=Prediction)
def predict(data: HeartData):
    features = pd.DataFrame([data.model_dump()], columns=model.feature_names_in_)
    prediction = model.predict(features)[0]
    return {"heart_disease": bool(prediction)}
