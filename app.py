import streamlit as st
import joblib
import numpy as np
from warnings import filterwarnings 
filterwarnings("ignore")
model = joblib.load("mymodel.joblib")

st.title("Sales Predictor App")

tv = st.slider("TV Investment",
               min_value = 0,
               max_value = 300,
               value = 150)
radio = st.slider("Radio Investment",
               min_value = 0,
               max_value = 300,
               value = 150)
newspaper = st.slider("Newspaper Investment",
               min_value = 0,
               max_value = 300,
               value = 150)
input_data = np.array(
    [
        [tv,radio,newspaper]
    ]
)
prediction = model.predict(input_data)
st.subheader(
    f"""Predicted sales.
    {prediction[0]:2f}"""
)
