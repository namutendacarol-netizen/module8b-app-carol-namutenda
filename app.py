"""Educational diabetes progression deployment."""
from pathlib import Path
import pickle
import pandas as pd
import streamlit as st
ROOT=Path(__file__).resolve().parent
st.set_page_config(page_title="Diabetes Progression Explorer",page_icon="📊")
@st.cache_resource
def load_artifact():
    # Only load the trusted model supplied with this project.
    with (ROOT/'model.pkl').open('rb') as f: return pickle.load(f)
try:
    a=load_artifact()
except (OSError,ValueError,ImportError,pickle.UnpicklingError) as exc:
    st.error(f"Model could not load: {exc}. Install requirements and run python train_model.py.")
    st.stop()
st.title("Diabetes Progression Explorer")
st.caption("Module 8B • Carol Namutenda • Public health model deployment")
st.info("Educational demonstration only. Not validated for diagnosis, treatment or use in Zambia's health services.")
st.write("Estimate the dataset's quantitative disease-progression score one year after baseline for people already living with diabetes. This does not predict whether someone has diabetes.")
profile=st.selectbox("Choose an example record",["Example 1","Example 2","Example 3"])
idx=int(profile[-1])-1
labels={"age":"Age (years)","sex":"Sex (dataset code)","bmi":"Body mass index","bp":"Average blood pressure","s1":"s1 — Total serum cholesterol","s2":"s2 — LDL","s3":"s3 — HDL","s4":"s4 — Total cholesterol / HDL","s5":"s5 — Serum triglyceride feature","s6":"s6 — Blood sugar feature"}
st.caption("Inputs use the dataset's original numeric scales. Sex codes are retained without assigning unverified labels. The exact meaning of some serum features is uncertain in the source documentation. Use the example records for this assignment.")
with st.form(f"inputs_{idx}"):
    cols=st.columns(2)
    values={}
    for i,name in enumerate(a['features']):
        with cols[i%2]:
            values[name]=st.number_input(labels[name],min_value=a['specs'][name]['min'],max_value=a['specs'][name]['max'],value=float(a['profiles'][idx][name]),format="%.3f",key=f"{idx}_{name}")
    go=st.form_submit_button("Predict progression")
if go:
    row=pd.DataFrame([values],columns=a['features'])
    result=float(a['model'].predict(row)[0])
    st.success("Prediction complete")
    st.write(f"Predicted progression score: {result:.1f}")
    st.caption("This is a dataset-specific score, not a percentage, blood glucose reading or clinical risk category. No clinical threshold is assigned.")
    st.write("Measurements used",row)
with st.expander("About the model and evaluation"):
    m=a['metrics']
    st.write("Model: StandardScaler + Ridge regression (alpha=10). Scaling is fitted on training records only.")
    st.write(f"442 records; {m['training_samples']} training and {m['test_samples']} test records. Random state 42.")
    st.write(f"Test MAE: {m['MAE']:.2f} score units; RMSE: {m['RMSE']:.2f}; R²: {m['R2']:.3f}.")
    st.write(f"Mean-only baseline MAE: {m['baseline_MAE']:.2f}. MAE is average absolute test error, not a confidence interval.")
    st.write("Small historical dataset; no external or Zambia-specific validation. Regression outputs can fall beyond the observed target range.")
    st.markdown("[Dataset documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes)")
