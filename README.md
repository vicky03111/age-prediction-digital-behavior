# Модель определения возраста по цифровому поведению

## О проекте
Проект посвящен созданию модели для определения возрастной категории пользователей на основе их цифрового следа. Это поможет показывать рекламу целевой аудитории.

## Данные
- users
- visits
- ads_activity
- surf_depth
- primary_device
- cloud_usage

## Структура репозитория
```text
age-prediction-digital-behavior/
├── README.md
├── requirements.txt
├── .gitignore
├── notebook.ipynb
└── utils.py
```
## Как запустить
pip install -r requirements.txt
jupyter notebook notebooks/02_modeling.ipynb

## Результаты
DummyClassifier: f1_macro = 0.094
Final LogisticRegression: f1_macro = 0.80

## Артефакты
models/final_model.joblib
models/preprocessor.joblib

## Автор
Пандей В.К.