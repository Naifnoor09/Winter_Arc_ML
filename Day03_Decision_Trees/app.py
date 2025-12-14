import pickle as pkl
import pandas as pd
import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "heart_disease_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pkl.load(f)

st.set_page_config(page_title="Heart Disease Predictor",page_icon="❤️", layout="wide")
st.title("AI Cardiologist: Heart Disease Risk")
st.write("Enter patient details below to get a prediction.")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=50)
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=200, value=120)
    chol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
    thalach = st.number_input("Max Heart Rate", min_value=50, max_value=250, value=150)
    oldpeak = st.number_input("ST Depression (Oldpeak)", min_value=0.0, max_value=10.0, value=1.0)
    
with col2:
    sex = st.selectbox("Sex (1 = Male, 0 = Female)", [0, 1])
    cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
    fbs = st.selectbox("Fasting Blood Sugar > 120 (1=True, 0=False)", [0, 1])
    restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
    exang = st.selectbox("Exercise Induced Angina (1=Yes, 0=No)", [0, 1])
    slope = st.selectbox("Slope of Peak Exercise (0-2)", [0, 1, 2])
    ca = st.selectbox("Major Vessels Colored by Fluoroscopy (0-3)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (0=Normal, 1=Fixed, 2=Reversable)", [0, 1, 2])


if st.button("Analyze Risk"):
    
    user_data = {
        "age": [age],
        "sex": [sex],
        "cp": [cp],
        "trestbps": [trestbps],
        "chol": [chol],
        "fbs": [fbs],
        "restecg": [restecg],
        "thalach": [thalach],
        "exang": [exang],
        "oldpeak": [oldpeak],
        "slope": [slope],
        "ca": [ca],
        "thal": [thal]
    }
    
    input_df = pd.DataFrame(user_data)
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("Result: High Risk of Heart Disease")
        st.write("Please consult a cardiologist.")
    else:
        st.success("Result: Healthy / Low Risk")