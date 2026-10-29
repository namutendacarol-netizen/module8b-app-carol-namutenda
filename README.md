# Diabetes Progression Explorer — Module 8B
**Author:** Carol Namutenda · **Repository:** `module8b-app-carol-namutenda`

## Purpose and technology
An interactive Streamlit app backed by a trained Ridge regression model. Python 3.12, pandas and scikit-learn; pinned dependencies in requirements.txt. The public scikit-learn Diabetes dataset contains 442 records and ten baseline features. The target is a quantitative disease-progression measure one year later among people already living with diabetes. It is not diabetes diagnosis or a probability.

## Training and evaluation
train_model.py loads raw features (scaled=False), splits 80/20 with random state 42, and fits StandardScaler + Ridge(alpha=10). Scaling learns only from training data. The 89 held-out records evaluate MAE, RMSE and R²; a mean-only baseline is also evaluated. See metrics.json and test_predictions.csv for actual results. model.pkl contains the fitted pipeline, feature order, example inputs and metadata. Only load trusted pickle files.

## Run in VS Code (Windows PowerShell)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```
Open http://localhost:8501. If .venv already exists from the Iris app, reuse it and skip its creation. Select an example record, review inputs and click **Predict progression**. The app displays a predicted score and input table. Expand the evaluation section to read test metrics. Example records avoid requiring real patient data.

## Reproduce and containerize
Retrain with `.\.venv\Scripts\python.exe train_model.py`. Run Docker Desktop, stop any local app using port 8501, then execute `docker compose up --build`. Open the same local URL. Stop with `docker compose down`. Docker uses Python 3.12 and the pinned requirements.

## Project repository
https://github.com/namutendacarol-netizen/module8b-app-carol-namutenda

## Limits and source
Educational only; no clinical thresholds, diagnostic claims or treatment guidance. Small historical dataset; no external or Zambia-specific validation. Raw numeric feature scales follow the source; some serum definitions are uncertain. Scores are not percentages. Source: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes (original study: Efron et al., 2004, Least Angle Regression).
