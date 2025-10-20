import pandas as pd
import joblib

class HeartRiskModel:
    """Класс для загрузки модели и выполнения предсказаний."""

    def __init__(self, model_path: str = "model.pkl"):
        """Загружаем сохранённую модель"""
        self.model = joblib.load(model_path)

    def predict(self, csv_path: str):
        """Принимает путь к CSV, делает предсказание и возвращает DataFrame"""
        data = pd.read_csv(csv_path)

        # Убираем таргет, если он случайно есть
        if "target" in data.columns:
            data = data.drop(columns=["target"])
            
        print("Колонки входного файла:", list(data.columns))
        print("Модель ожидает:", self.model.feature_names_in_)
        preds = self.model.predict(data)

        result = pd.DataFrame({
            "id": data["id"] if "id" in data.columns else range(1, len(preds) + 1),
            "prediction": preds
        })

        return result