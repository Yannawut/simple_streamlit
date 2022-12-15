import streamlit as st
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from pathlib import Path
import os

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
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
    st.write(os.listdir(os.curdir))

    # If button is pressed
    if st.button("Submit"):
        
        # Unpickle classifier
        clf = pickle.load(open("car_pred_model.pkl", 'rb'))
        
        # Store inputs into dataframe
        X = pd.DataFrame([[Year, Present_Price, Driven_kms, Fuel_Type, Selling_Type,
        Transmission, Owner]], 
                        columns = ['Year', 'Present_Price', 'Driven_kms', 'Fuel_Type', 'Selling_type',
            'Transmission', 'Owner'],)
        
        # Get prediction
        prediction = clf.predict(X)[0]
        
        # Output prediction
        st.text(f"Predicted car price is {prediction}")
