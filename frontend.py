import streamlit as st
import requests

API_URL="http://16.178.42.100:8000/predict"

st.title("Insurance Premium Predictor")
st.markdown("Enter your details below")

#Input Fields
age=st.number_input("Age",min_value=1,max_value=120,value=30)
weight=st.number_input("Weight (in Kgs)",min_value=1.0,value=65.0)
height=st.number_input("Height (in meters)",min_value=0.5,max_value=2.2,value=1.8)
income_lpa=st.number_input("Annual Income in LPA",value=6.0,min_value=1.0)
smoker=st.selectbox("Are you a smoker?",options=[True,False])
city=st.text_input("City of resident",value="Mumbai")
occupation=st.selectbox("Occupation",options=['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])

if st.button("Predict the premium category"):
    input_data={
        "age":age,
        "weight":weight,
        "height":height,
        "income_lpa":income_lpa,
        "smoker":smoker,
        "city":city,
        "occupation":occupation
    }
    try:
        response=requests.post(API_URL,json=input_data)
        result=response.json()
        if response.status_code==200 and "response" in result:
            prediction=result["response"]
            st.success(f"Predicted Insurance Premium Category is **{prediction['predicted_category']}**")
            st.write("Confidence",prediction["confidence"])
            st.write("Class Probabilities:")
            st.json(prediction["class_probabalities"])
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)
    except requests.exceptions.ConnectionError:
        st.error("Could not connet to the FastAPI server. Make sure it's Running")