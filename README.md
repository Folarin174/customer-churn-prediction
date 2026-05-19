# 📊 Customer Churn Prediction

A machine learning web application that predicts whether a telecom customer will churn based on their account details and usage patterns.

🔗 **Live App:** [customer-churn-prediction-kcgutw5v7vzq8cjafkapp7e.streamlit.app](https://customer-churn-prediction-kcgutw5v7vzq8cjafkapp7e.streamlit.app)

---

## 📌 Project Overview

Customer churn is one of the biggest challenges in the telecom industry. This project builds a machine learning model to identify customers at risk of leaving, enabling businesses to take proactive retention action.

---

## 📂 Dataset

- **Source:** [Telco Customer Churn - Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Size:** 7,043 customers, 21 features
- **Target:** Churn (Yes/No)

---

## 🔍 Project Steps

1. **Exploratory Data Analysis (EDA)** — explored data types, missing values, duplicates and distributions
2. **Data Preprocessing** — fixed TotalCharges column, encoded categorical variables, removed irrelevant features
3. **Model Training** — trained Logistic Regression and Random Forest models
4. **Model Evaluation** — evaluated using Accuracy, Confusion Matrix, Classification Report and ROC AUC Score
5. **Deployment** — deployed as an interactive web app using Streamlit

---

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 82% |
| ROC AUC Score | 86.14% |
| Precision (Churn) | 68% |
| Recall (Churn) | 58% |
| F1 Score (Churn) | 62% |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas & NumPy | Data manipulation |
| Matplotlib & Seaborn | Data visualization |
| Scikit-learn | Model training and evaluation |
| Joblib | Model serialization |
| Streamlit | Web app deployment |
| GitHub | Version control |

---

## 🚀 Run Locally

1. Clone the repository:
```bash
git clone https://github.com/Folarin174/customer-churn-prediction.git
cd customer-churn-prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
customer-churn-prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── app.py                  # Streamlit web app
├── churn.ipynb             # Full analysis notebook
├── model.pkl               # Trained ML model
├── scaler.pkl              # Feature scaler
└── requirements.txt        # Project dependencies
```

---

## 💡 Key Insights

- Customers on **Month-to-month contracts** are most likely to churn
- Customers with **Fiber optic internet** have higher churn rates
- Customers with **longer tenure** are less likely to churn
- **Electronic check** payment method is associated with higher churn

---

## 👤 Author

**Umar Musa (Folarin174)**
- GitHub: [@Folarin174](https://github.com/Folarin174)
