import pickle
import streamlit as st

model1=pickle.load(open("area.pkl","rb"))

def myf1():
    area=st.number_input("Enter the area value....")
    pred= st.button("Predict")
    if pred:
        op=model1.predict([[area]])
        st.write("Price of the area is: ",op)

myf1()