from fastapi import FastAPI, UploadFile, File
from model import HeartRiskModel
import tempfile

app = FastAPI(
    title="Heart Risk Predictor",
    description="FastAPI приложение для предсказания риска сердечных заболеваний",
    version="1.0.0"
)

# Загружаем модель при запуске
model = HeartRiskModel("model.pkl")


@app.get("/health")
def health():
    """Проверка, что сервис жив"""
    return {"status": "OK"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Принимает CSV и возвращает предсказания"""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    preds = model.predict(tmp_path)
    return preds.to_dict(orient="records")