from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class HeartData(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)

    age: int = Field(gt=0, le=120)
    sex: Literal[0, 1]
    cp: Literal[0, 1, 2, 3]
    trestbps: float = Field(gt=0)
    chol: float = Field(gt=0)
    fbs: Literal[0, 1]
    restecg: Literal[0, 1, 2]
    thalach: float = Field(gt=0)
    exang: Literal[0, 1]
    oldpeak: float = Field(ge=0)
    slope: Literal[0, 1, 2]
    ca: Literal[0, 1, 2, 3, 4]
    thal: Literal[0, 1, 2, 3]


class Prediction(BaseModel):
    heart_disease: bool
