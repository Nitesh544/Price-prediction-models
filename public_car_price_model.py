# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

with open ('carprice_prediction_model.sav','rb') as f:
    car_model=pickle.load(f)
    
with st.sidebar :
    selectied = option_menu("Multiple Price Prediction System using ML",
                            ['Car Price Prediction','Upcomming'],
                            icons=['truck','caret-up-square'],
                            default_index=0)
    
if (selectied=='Car Price Prediction') :
    st.title ("Car Price Prediction using ML")
    Mileage=st.text_input("Enter milage count")
    Age=st.text_input("Enter Car Age")
    AudiA5	=st.text_input("Enter car code1")
    BMWX5=st.text_input("Enter cae code2")
    
    
    price_predict=''
    
    if st.button("Car prediction results"):
       price_predict= car_model.predict([[Mileage,Age,AudiA5,BMWX5]])
    
    
    st.success(price_predict)
    
if (selectied=='Upcomming') :
    st.title ("Stay Tuned")
    
