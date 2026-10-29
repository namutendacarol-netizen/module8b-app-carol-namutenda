"""Reproducible health model: raw features, training-only scaling."""
from pathlib import Path
import json, pickle
import sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
ROOT = Path(__file__).resolve().parent

def train():
    data = load_diabetes(as_frame=True, scaled=False)
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    model = make_pipeline(StandardScaler(), Ridge(alpha=10.0))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    baseline = DummyRegressor().fit(X_train,y_train).predict(X_test)
    metrics = {"dataset":"scikit-learn Diabetes", "samples":442,
       "training_samples":len(X_train), "test_samples":len(X_test), "random_state":42,
       "MAE":mean_absolute_error(y_test,pred), "RMSE":root_mean_squared_error(y_test,pred),
       "R2":r2_score(y_test,pred), "baseline_MAE":mean_absolute_error(y_test,baseline),
       "sklearn_version":sklearn.__version__}
    specs = {name:{"min":float(data.data[name].min()), "max":float(data.data[name].max())} for name in data.feature_names}
    profiles = X_test.iloc[:3].to_dict(orient="records")
    artifact = {"model":model,"features":list(data.feature_names),"specs":specs,"profiles":profiles,"metrics":metrics}
    with (ROOT/'model.pkl').open('wb') as f: pickle.dump(artifact,f)
    (ROOT/'metrics.json').write_text(json.dumps(metrics,indent=2))
    data.frame.to_csv(ROOT/'diabetes_data.csv',index=False)
    pd = __import__('pandas')
    pd.DataFrame({"observed":y_test,"predicted":pred}).to_csv(ROOT/'test_predictions.csv',index=False)
    print(json.dumps(metrics,indent=2))
if __name__ == '__main__': train()
