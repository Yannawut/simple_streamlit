import streamlit as st
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from pathlib import Path

# Title
st.header("Car price prediction App")

# Input bar
Year = st.number_input("Enter Year")
Present_Price = st.number_input("Enter Present_Price")
Driven_kms = st.number_input("Enter Driven_kms")
Owner = st.number_input("Enter Owner")

# Dropdown input
Fuel_Type = st.selectbox("Select Fuel_Type", (0, 1, 2))
Selling_Type = st.selectbox("Select Selling_Type", (0, 1))
Transmission = st.selectbox("Select Transmission", (0, 1))

pkl_path = 'simple_streamlit/car_pred_model.pkl'

# If button is pressed
if st.button("Submit"):
    
    # Unpickle classifier
    clf = pickle.load(open(pkl_path, 'rb'))
    
    # Store inputs into dataframe
    X = pd.DataFrame([[Year, Present_Price, Driven_kms, Fuel_Type, Selling_Type,
       Transmission, Owner]], 
                     columns = ['Year', 'Present_Price', 'Driven_kms', 'Fuel_Type', 'Selling_type',
        'Transmission', 'Owner'],)
    
    # Get prediction
    prediction = clf.predict(X)[0]
    
    # Output prediction
    st.text(f"Predicted car price is {prediction}")
