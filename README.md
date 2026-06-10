# 🏦 Loan Approval & Credit Risk Intelligent System

**[🚀 View Live Project Demo Here](https://loan-risk-intelligent-system-efjkhilyybpngkz6lqtngq.streamlit.app/)**

![App Overview](images/Screenshot%202026-06-11%20004503.png)

## 📌 Overview
The **Loan Approval & Credit Risk Intelligent System** is a full-stack, data-driven machine learning application created to assess the default risk of an applicant by predicting the probability of default based on an array of financial, employment, and current credit properties. This tool harnesses the power of predictive ML combined with Explainable AI (SHAP) to categorize borrowers into risk bands and highlight the top reasons for that risk assessment in real time, bringing transparency to loan approval processes.

## ✨ Key Deliverables
- **Default Probability Prediction**: Accurately scores the percentage likelihood of an applicant defaulting based on their financial metrics (calculators internally scale local currency metrics against real-time variables).
- **Risk Categorization**: Segments users based on their scores into intuitive risk bands (e.g., Very Low Risk, Moderate Risk, Very High Risk).
- **Explainable AI with SHAP**: Integrates SHAP's TreeExplainer to dynamically provide the top 5 contributing factors to every individual prediction, ensuring decisions are interpretable.
- **Deployment Ready ML Pipeline**: Employs an end-to-end `scikit-learn` pipeline, preserving data transformation robustness from training to real-time inference.

---

## 📸 App Showcase

| Data Entry & Details | Real-Time Predictions & Explainability |
|:---:|:---:|
| <img src="images/Screenshot%202026-06-11%20004530.png" width="400"> | <img src="images/Screenshot%202026-06-11%20004739.png" width="400"> |
| <img src="images/Screenshot%202026-06-11%20004912.png" width="400"> | <img src="images/Screenshot%202026-06-11%20005133.png" width="400"> |

*(Note: Click on images to view them in full resolution)*

---

## 🏗️ Architecture & Tech Stack

- **Machine Learning**: `scikit-learn` & `pandas` for preprocessing, pipeline building, data manipulation, and predictive tree-based modeling.
- **Explainable AI**: `shap` framework deeply integrated via the backend for interpretability.
- **Backend RESTful API**: `FastAPI` powers a high-performance backend serving the risk model.
- **Frontend Dashboard**: A highly interactive `Streamlit` application.

## 📊 Key Findings from Data Modeling
During the EDA and model training phase targeting historical LendingClub data, several pivotal findings shaped this tool:
1. **Credit-related Variables Dominate**: Credit history elements carried immense predictive signal compared to sheer qualitative labels.
2. **Borrower Financial Health Matters**: Debt-to-income and utilization metrics heavily alter trajectories.
3. **Loan Structure is Critical**: Variables related to term, purpose, and total amount fundamentally influence outcomes.
4. **Algorithmic Edge**: Tree-based estimators offered a modest, yet statistically significant improvement over linear baseline paradigms.
5. **Beyond Simple Grades**: Crucially, actionable and powerful predictive signal exists well beyond relying solely on provided LendingClub risk grades.
6. **Thresholds & Trade-offs**: Any threshold selection for classification fundamentally creates business-level trade-offs between approval volumes and loss safety.

## ⚠️ Known Limitations
While performing robustly against offline test batches, the system inherently encompasses natural ML boundaries within the domain of economics:
1. **Single Platform Reliance**: Models trained solely on singular platform history lack resilience to divergent financial ecosystems.
2. **Historical Constraints**: Training data captures static historical patterns that might fail to generalize given entirely new socioeconomic trends.
3. **Economic Sensitivity**: Macro-level economic conditions possess the ability to shift arbitrarily, severely impacting borrower reliability indiscriminately.
4. **Data Drift Susceptibility**: Economic characteristics of populations drift over time, which will steadily degrade the model's performance without scheduled retraining.
5. **Model Uncertainty**: Deep uncertainty persists – individual catastrophic life events causally triggering defaults reside largely outside the structured features available to the system.

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and ensure your local Python environment is at standard versions (3.9+). 
```bash
pip install -r requirements.txt
```

### 2. Backend (FastAPI Model Service)
Navigate to the root directory and start the inference API server with:
```bash
uvicorn api.main:app --reload
```
The FastAPI instance will be available at `http://localhost:8000`. 
Native SwaggerUI documentation will be exposed at `http://localhost:8000/docs` to test endpoints manually.

### 3. Frontend (Streamlit Dashboard)
To run the interactive UI dashboard, open a separate terminal window and execute:
```bash
cd streamlit-app
streamlit run app.py
```
Your browser will automatically launch the Streamlit frontend. Enter borrower details, confirm submission, and evaluate real-time intelligent risk scoring and interpretable feature impacts!

---
*Developed as an intelligent, transparent, and capable proof of concept for assessing lending risk.*
