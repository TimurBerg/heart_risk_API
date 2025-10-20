```
heart_risk_model/
│
├── notebooks/
│   └── heart_risk_model.ipynb         # Jupyter-тетрадь с исследованием и обучением модели
│
├── model/
│   ├── model.py                       # Класс модели для FastAPI (логика предсказаний)
│   └── model.pkl                      # Сохранённая модель (через joblib)                 
│
├── api/
│   ├── app.py                         # FastAPI приложение
│   └── API_test.csv                   # Пример тестовых данных (X_train из тетради)
│
├── data/
│   └── predictions.csv                # Финальные предсказания на тестовых данных
│
├── requirements.txt                   # зависимости (для FastAPI и ML)
└── README.md                          # описание проекта
```