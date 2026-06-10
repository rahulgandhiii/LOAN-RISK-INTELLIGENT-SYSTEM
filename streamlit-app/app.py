import streamlit as st
import requests

st.title("Loan Risk Intelligent System")
st.header("Applicant Details: ")

loan_amt=st.number_input("Loan Amount (₹)",50000,10000000,500000)
term=st.selectbox("Term", ["36 months", "60 months"])
purpose=st.selectbox("Purpose", ["debt_consolidation", "credit_card", 
                                 "home_improvement", "other",
                                 "major_purchase", "medical",
                                 "small_business", "car", "vacation",
                                 "moving", "house", "wedding", 
                                 "renewable_energy","educational"])
annual_inc=st.number_input("Annual Income (₹)",100000,100000000,1000000)
emp_length=st.selectbox("Employment Length (years)", ["< 1 year",
                                                         "1 year","2 years",
                                                         "3 years","4 years",
                                                         "5 years","6 years",
                                                         "7 years","8 years",
                                                         "9 years","10+ years"])
home_ownership=st.selectbox("Home Ownership", ["RENT", "OWN",
                                               "MORTGAGE", "OTHER",
                                               "NONE", "ANY"])
verification_status=st.selectbox("Verification Status", ["Verified",
                                                         "Source Verified", 
                                                         "Not Verified"])
dti=st.slider("Debt to Income Ratio", 0.0, 50.0, 20.0, step=0.1)
credit_score=st.number_input("Credit Score", 300, 850, 650)
revol_bal=st.number_input("Outstanding Credit Balance (₹)",0,10000000,100000)
revol_util=st.slider("Credit Utilization (%)", 0.0, 100.0, 30.0, step=0.1)
total_acc = st.number_input("Total Accounts", 0, 100, 20)
mort_acc = st.number_input("Mortgage Accounts", 0, 10, 1)
open_acc = st.number_input("Open Accounts", 0, 50, 5)
delinq_2yrs = st.number_input("Delinquencies (2 yrs)", 0, 10, 0)
pub_rec = st.number_input("Public Records", 0, 10, 0)
pub_rec_bankruptcies = st.number_input("Bankruptcies", 0, 5, 0)
credit_history_years = st.number_input("Credit History (years)", 0, 50, 8)

USD_INR = 85.0
loan_amt_usd=loan_amt/USD_INR
annual_inc_usd=annual_inc/USD_INR
revol_bal_usd=revol_bal/USD_INR

if st.button("Predict Risk"):
    data={
        "loan_amnt": loan_amt_usd,
        "term": term,
        "purpose": purpose,
        "annual_inc": annual_inc_usd,
        "emp_length": emp_length,
        "home_ownership": home_ownership,
        "verification_status": verification_status,
        "dti": dti,
        "fico_range_low": credit_score-2,
        "fico_range_high": credit_score+2,
        "revol_bal": revol_bal_usd ,
        "revol_util": revol_util,
        "total_acc": total_acc,
        "mort_acc": mort_acc,
        "open_acc": open_acc,
        "delinq_2yrs": delinq_2yrs,
        "pub_rec": pub_rec,
        "pub_rec_bankruptcies": pub_rec_bankruptcies,
        "credit_history_years": credit_history_years
    }
    response=requests.post("http://127.0.0.1:8000/predict", json=data)
    if response.status_code == 200:
        result = response.json()
    else:
        st.error("Prediction failed")
    st.subheader("Result")
    prob_default = result["Probability_default"]
    st.metric("Default Probability", f"{prob_default:.1%}")
    st.progress(int(prob_default*100))
    if result["Risk_Band"] in ["Low Risk", "Very Low Risk"]:
        st.success("Risk Band: " + result["Risk_Band"])
    elif result["Risk_Band"] in ["Moderate Risk"]:
        st.warning("Risk Band: " + result["Risk_Band"])
    else:
        st.error("Risk Band: " + result["Risk_Band"])
    st.subheader("Top Risk Factors")
    for feature in result["Top_Risk_Factors"]:
        st.write("-", feature)