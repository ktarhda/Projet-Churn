import streamlit as st
import pandas as pd
import joblib
import numpy as np
import streamlit as st

# Charger modèle et features
model = joblib.load("churn_model.pkl")
feature_names = joblib.load("features.pkl")

st.title("Prédiction de churn clients (Telco)")

contract_mapping = {
    "Mois par mois": "Month-to-month",
    "Un an": "One year",
    "Deux ans": "Two year"
}
# Les input
gender = st.selectbox("Genre", ["Male", "Female"])
senior = st.selectbox("Client senior", [0, 1])
tenure = st.slider("Ancienneté (mois)", 0, 72, 12)
contract = st.selectbox("Contrat", ["Mois par mois", "Un an", "Deux ans"])
monthly = st.number_input("Facturation mensuelle en $", min_value=0.0, value=50.0)

if st.button("Prédire"):
    
    df = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "tenure": tenure,
        "Contract": contract_mapping[contract],
        "MonthlyCharges": monthly,
       
    }])

    # One‑hot encoding identique au notebook
    df = pd.get_dummies(df)
    # Réaligner sur les colonnes du training
    df = df.reindex(columns=feature_names, fill_value=0)

    proba = model.predict_proba(df)[0, 1]
    proba_pct = proba * 100 
    # seuil ajustable si besoin
    seuil = 0.5
    if proba >= seuil:
        st.error(f"Client susceptible de churn à {proba_pct:.1f}%")
    else:
        st.success(f"Client fidèle à {proba_pct:.1f}%")
