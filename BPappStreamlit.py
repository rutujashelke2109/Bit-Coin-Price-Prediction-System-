import joblib
import streamlit as st 
import numpy as np

model= joblib.load(r'C:\RUTUJA\bitcoin_price_prediction.pkl')

st.title("Bitcoin Price Prediction")

a=st.number_input("Enter open-close price: ")
b=st.number_input("Enter low-high price: ")
c=st.number_input("Enter quater_end value(0,1): ")


if st.button('Predict'):
    cus_input= np.array([[a,b,c]])
    result= model.predict(cus_input)
    prediction=int(round(result[0]))
    prices=""
    if prediction == 0:
        prices=('prices goes down')
    elif prediction == 1:
        prices=('prices goes up')
    else:
        prices=('can not  predict')
    st.success(f"The predicted price is: {prices}")









    