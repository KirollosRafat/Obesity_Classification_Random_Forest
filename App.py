import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

def main():
    # Set up the inputs
    st.title("Obesity Classification Using Classic ML")
    age = st.number_input("Age",value=0.00)
    Gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    Height = st.number_input("Height",value=0.00)    
    Weight = st.number_input("Weight",value=0.00)
    BMI = st.number_input("BMI",value=0.00)

    # Convert the inputs into one numpy array 
    features = np.array([[age, Gender, Height, Weight, BMI]])

    if st.button("Predict"):
        prediction = model.predict(features)[0]
        if prediction == 0:
            st.success("Normal Weight")
        elif prediction == 1:
            st.success("Obese")    
        elif prediction == 2:
            st.success("Overweight")
        else:
            st.success("Underweight")

if __name__ == "__main__":
    main()