from fastapi import FastAPI
import joblib
import pandas as pd
from api.utils import risk_band, applicant_to_dataframe
from api.schemas import Applicant
import shap

app=FastAPI(title="Credit Loan Risk Prediction API")
model=joblib.load("models/user_model.pkl")
explainer=shap.TreeExplainer(model.named_steps['classifier'])

@app.get("/")
def home():
    return {"message":"Welcome to Credit Loan Risk Prediction API"}

@app.post("/predict")
def predict(applicant: Applicant):
    applicant_df=applicant_to_dataframe(applicant)
    X_transformed = (model.named_steps["preprocess"].transform(applicant_df))
    shap_values = explainer.shap_values(X_transformed)
    sample_shap=shap_values[0]
    features=model.named_steps["preprocess"].get_feature_names_out()
    shap_df=pd.DataFrame({"feature": features,"shap_value": sample_shap})
    shap_df["abs_value"]=(shap_df["shap_value"].abs())
    shap_df=(shap_df.sort_values("abs_value",ascending=False))
    top5=shap_df.head(5)

    probability=model.predict_proba(applicant_df)[0][1]
    risk=risk_band(probability)
    return{
        "Probability_default": round(float(probability),4),
        "Risk_Band": risk,
        "Top_Risk_Factors": top5["feature"].tolist()
    }

