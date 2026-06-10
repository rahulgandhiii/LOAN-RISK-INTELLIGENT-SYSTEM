import pandas as pd

def risk_band(probability):
    if probability < 0.20:
        return "Very Low Risk"
    elif probability < 0.375:
        return "Low Risk"
    elif probability < 0.5:
        return "Moderate Risk"
    elif probability < 0.65:
        return "High Risk"
    else:
        return "Very High Risk"

def applicant_to_dataframe(applicant):
    data = {
        "loan_amnt": [applicant.loan_amnt],
        "term": [applicant.term],
        "purpose": [applicant.purpose],
        "annual_inc": [applicant.annual_inc],
        "emp_length": [applicant.emp_length],
        "home_ownership": [applicant.home_ownership],
        "verification_status": [applicant.verification_status],
        "dti": [applicant.dti],
        "fico_range_low": [applicant.fico_range_low],
        "fico_range_high": [applicant.fico_range_high],
        "delinq_2yrs": [applicant.delinq_2yrs],
        "pub_rec": [applicant.pub_rec],
        "pub_rec_bankruptcies": [applicant.pub_rec_bankruptcies],
        "revol_bal": [applicant.revol_bal],
        "revol_util": [applicant.revol_util],
        "total_acc": [applicant.total_acc],
        "mort_acc": [applicant.mort_acc],
        "open_acc": [applicant.open_acc],
        "credit_history_years": [applicant.credit_history_years]
    }
    return pd.DataFrame(data)