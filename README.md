# Heart Disease Prediction API

A simple FastAPI app that predicts heart disease using Logistic Regression.

GitHub repository: [Chowx30/heart-disease-api](https://github.com/Chowx30/heart-disease-api).

## Dataset and model

Dataset: [Heart Disease Dataset on Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset).

The original CSV is included in `data/heart.csv`. It contains 1,025 rows. Duplicate rows are removed before an 80/20 train/test split, leaving 302 unique rows. The model uses StandardScaler and Logistic Regression. The saved model is in `model/heart_model.joblib`.

The target is `0` for absence and `1` for presence. This is an educational project, not a medical diagnosis tool.

Test accuracy: **80.33%** on 61 test rows, using 241 training rows.

## Project files

```text
app/
  __init__.py
  main.py
  schemas.py
data/
  heart.csv
model/
  heart_model.joblib
  info.json
Dockerfile
docker-compose.yml
requirements.txt
render.yaml
sample.json
train_model.py
README.md
```

## Run with Docker

Install and start Docker Desktop. Open a terminal in this project folder and run:

```bash
docker compose build
docker compose up
```

The older commands `docker-compose build` and `docker-compose up` also work if that version of Compose is installed.

Open [Swagger UI](http://localhost:8000/docs). To stop the app, press Ctrl+C and run `docker compose down`.

## Run with Python

Use Python 3.13:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

On Windows, activate the environment with `.venv\Scripts\activate`.

The trained model is already included. To train it again:

```bash
python train_model.py
```

## Endpoints

| Method | Path | Result |
| --- | --- | --- |
| GET | `/health` | App status |
| GET | `/info` | Model type, features, and test accuracy |
| POST | `/predict` | `heart_disease: true` or `false` |

The 13 input features are `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, and `thal`. Use the dataset's numeric encoding. All features are required.

## Test the API

Run these from the project folder while the app is running:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/info
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d @sample.json
```

The sample request returns `{"heart_disease": false}`. Invalid or missing features return HTTP 422.

You can also open `/docs`, expand `POST /predict`, select **Try it out**, paste the contents of `sample.json`, and click **Execute**.

## Deploy on Render

1. Upload all project files to a GitHub repository, including the saved model. Include the hidden `.dockerignore` and `.gitignore` files.
2. Sign in to [Render](https://dashboard.render.com/) and choose **New → Web Service**.
3. Connect the GitHub repository, or use its public Git URL.
4. Choose **Docker** as the language/runtime and the **Free** instance if available.
5. Leave the root directory empty. Use `./Dockerfile` for the Dockerfile path and `.` for the build context.
6. Set the health check path to `/health`. Leave the Docker start command empty; the Dockerfile already starts the app using Render's `PORT`.
7. Click **Deploy Web Service** and wait for the service to become live.
8. Open the service URL with `/health`, `/info`, and `/docs`. Test `/predict` using the Swagger UI or the curl command above with the live URL.

The included `render.yaml` can also be used with **New → Blueprint**.

## Submission

Submit these two links on the assignment page:

- GitHub repository URL containing this project.
- Live Render service URL.

Before submitting, confirm the repository is public or accessible to your instructor, the model file is uploaded, and the live `/docs` and `/predict` endpoints work. Paste the two links into the assignment submission box and submit.

## References

- [FastAPI request bodies](https://fastapi.tiangolo.com/tutorial/body/)
- [Docker Compose](https://docs.docker.com/compose/gettingstarted/)
- [Docker on Render](https://render.com/docs/docker)
