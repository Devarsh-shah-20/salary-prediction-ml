import streamlit as st
import pandas as pd
import joblib

model = joblib.load("salary_prediction_model.pkl")

st.title("💼 Salary Prediction App")
st.write("Enter employee details to predict salary")

age = st.number_input("Age", 18, 65, 30)
experience = st.number_input("Experience Years", 0, 40, 5)

gender = st.selectbox("Gender", ["Male", "Female"])
department = st.selectbox("Department", ["Finance", "HR", "Marketing", "Product", "Sales"])
job_title = st.selectbox("Job Title", ["Engineer", "Executive", "Intern", "Manager"])
education = st.selectbox("Education Level", ["Bachelor", "Master", "PhD"])
location = st.selectbox("Location", ["Chicago", "New York", "San Francisco", "Seattle", "Austin"])

input_data = pd.DataFrame(columns=model.feature_names_in_)
input_data.loc[0] = 0

input_data["Age"] = age
input_data["Experience_Years"] = experience

if gender == "Male":
    input_data["Gender_Male"] = 1

for field, value in {
    "Department": department,
    "Job_Title": job_title,
    "Education_Level": education,
    "Location": location
}.items():
    col_name = f"{field}_{value}"
    if col_name in input_data.columns:
        input_data[col_name] = 1

if st.button("Predict Salary"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Salary: ${prediction[0]:,.2f}")