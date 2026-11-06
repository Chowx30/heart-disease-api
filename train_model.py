import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from app.schemas import HeartData

base_dir = Path(__file__).resolve().parent
data = pd.read_csv(base_dir / "data" / "heart.csv").drop_duplicates()
features = list(HeartData.model_fields)
X = data[features]
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
accuracy = accuracy_score(y_test, model.predict(X_test))

model_dir = base_dir / "model"
model_dir.mkdir(exist_ok=True)
joblib.dump(model, model_dir / "heart_model.joblib")

info = {
    "model_type": "Logistic Regression",
    "features": features,
    "test_accuracy": round(accuracy, 4),
    "training_rows": len(X_train),
    "test_rows": len(X_test),
    "target": {"0": "absence", "1": "presence"},
}
(model_dir / "info.json").write_text(json.dumps(info, indent=2) + "\n")
print(f"Test accuracy: {accuracy:.2%}")
print("Model saved to model/heart_model.joblib")
