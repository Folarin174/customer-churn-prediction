import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

st.title('📊 Customer Churn Predictor')
st.write('Enter customer details below to predict whether they will churn.')

st.sidebar.header('Customer Details')

gender = st.sidebar.selectbox('Gender', ['Female', 'Male'])
senior = st.sidebar.selectbox('Senior Citizen', ['No', 'Yes'])
partner = st.sidebar.selectbox('Has Partner', ['No', 'Yes'])
dependents = st.sidebar.selectbox('Has Dependents', ['No', 'Yes'])
tenure = st.sidebar.slider('Tenure (months)', 0, 72, 12)
phone_service = st.sidebar.selectbox('Phone Service', ['No', 'Yes'])
multiple_lines = st.sidebar.selectbox('Multiple Lines', ['No', 'Yes', 'No phone service'])
internet_service = st.sidebar.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
online_security = st.sidebar.selectbox('Online Security', ['No', 'Yes', 'No internet service'])
online_backup = st.sidebar.selectbox('Online Backup', ['No', 'Yes', 'No internet service'])
device_protection = st.sidebar.selectbox('Device Protection', ['No', 'Yes', 'No internet service'])
tech_support = st.sidebar.selectbox('Tech Support', ['No', 'Yes', 'No internet service'])
streaming_tv = st.sidebar.selectbox('Streaming TV', ['No', 'Yes', 'No internet service'])
streaming_movies = st.sidebar.selectbox('Streaming Movies', ['No', 'Yes', 'No internet service'])
contract = st.sidebar.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.sidebar.selectbox('Paperless Billing', ['No', 'Yes'])
payment_method = st.sidebar.selectbox('Payment Method', [
    'Bank transfer (automatic)', 'Credit card (automatic)',
    'Electronic check', 'Mailed check'])
monthly_charges = st.sidebar.slider('Monthly Charges ($)', 18.0, 120.0, 65.0)
total_charges = st.sidebar.slider('Total Charges ($)', 0.0, 9000.0, 2000.0)

def encode(val, options):
    return options.index(val)

input_data = np.array([[
    encode(gender, ['Female', 'Male']),
    1 if senior == 'Yes' else 0,
    encode(partner, ['No', 'Yes']),
    encode(dependents, ['No', 'Yes']),
    tenure,
    encode(phone_service, ['No', 'Yes']),
    encode(multiple_lines, ['No', 'No phone service', 'Yes']),
    encode(internet_service, ['DSL', 'Fiber optic', 'No']),
    encode(online_security, ['No', 'No internet service', 'Yes']),
    encode(online_backup, ['No', 'No internet service', 'Yes']),
    encode(device_protection, ['No', 'No internet service', 'Yes']),
    encode(tech_support, ['No', 'No internet service', 'Yes']),
    encode(streaming_tv, ['No', 'No internet service', 'Yes']),
    encode(streaming_movies, ['No', 'No internet service', 'Yes']),
    encode(contract, ['Month-to-month', 'One year', 'Two year']),
    encode(paperless_billing, ['No', 'Yes']),
    encode(payment_method, [
        'Bank transfer (automatic)', 'Credit card (automatic)',
        'Electronic check', 'Mailed check']),
    monthly_charges,
    total_charges
]])

input_scaled = scaler.transform(input_data)

if st.button('🔮 Predict Churn'):
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]

    if prediction == 1:
        st.error(f'⚠️ This customer is LIKELY TO CHURN!')
        st.metric('Churn Probability', f'{round(probability[1] * 100, 1)}%')
    else:
        st.success(f'✅ This customer is NOT likely to churn.')
        st.metric('Retention Probability', f'{round(probability[0] * 100, 1)}%')

    st.subheader('Prediction Breakdown')
    col1, col2 = st.columns(2)
    col1.metric('Churn Risk', f'{round(probability[1] * 100, 1)}%')
    col2.metric('Retention', f'{round(probability[0] * 100, 1)}%')