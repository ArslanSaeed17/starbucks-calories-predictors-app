
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Starbucks Calories Predictor",
    page_icon="☕"
)

@st.cache_resource
def load_model():
    return joblib.load("starbucks_calories_model.pkl")

model = load_model()

st.title("☕ Starbucks Calories Predictor")
st.write("Enter the nutritional values to predict drink calories.")

with st.form("prediction_form"):
    trans_fat = st.number_input("Trans Fat (g)", min_value=0.0, value=0.0)
    saturated_fat = st.number_input("Saturated Fat (g)", min_value=0.0, value=0.0)
    sodium = st.number_input("Sodium (mg)", min_value=0.0, value=0.0)
    carbs = st.number_input("Total Carbohydrates (g)", min_value=0.0, value=0.0)
    cholesterol = st.number_input("Cholesterol (mg)", min_value=0.0, value=0.0)
    fibre = st.number_input("Dietary Fibre (g)", min_value=0.0, value=0.0)
    sugars = st.number_input("Sugars (g)", min_value=0.0, value=0.0)
    protein = st.number_input("Protein (g)", min_value=0.0, value=0.0)

    submitted = st.form_submit_button("Predict Calories")

if submitted:
    features = pd.DataFrame([[
        trans_fat,
        saturated_fat,
        sodium,
        carbs,
        cholesterol,
        fibre,
        sugars,
        protein
    ]], columns=[
        "Trans Fat (g) ",
        "Saturated Fat (g)",
        " Sodium (mg)",
        " Total Carbohydrates (g) ",
        "Cholesterol (mg)",
        " Dietary Fibre (g)",
        " Sugars (g)",
        " Protein (g) "
    ])

    prediction = model.predict(features)[0]
    st.success(f"Predicted Calories: {prediction:.1f}")
