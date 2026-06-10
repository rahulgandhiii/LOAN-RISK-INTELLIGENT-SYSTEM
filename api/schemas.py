from pydantic import BaseModel
class Applicant(BaseModel):
    loan_amnt: float
    term: str
    purpose: str
    annual_inc: float
    emp_length: str
    home_ownership: str
    verification_status: str
    dti: float
    fico_range_low: float
    fico_range_high: float
    delinq_2yrs: int
    pub_rec: int
    pub_rec_bankruptcies: int
    revol_bal: float
    revol_util: float
    total_acc: int
    mort_acc: int
    open_acc: int
    credit_history_years: float
    