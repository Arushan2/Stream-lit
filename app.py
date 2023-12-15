import streamlit as st
x = st.number_input("Insert total marks as your sub scheme", value=None)
y = st.number_input("Insert total marks as your main scheme", value=None)
name=st.text_input("Enter your Name")
stmarks=st.number_input("Insert student's marks", value=None)
butt=st.button("Submit")

# def calculate(x,y,z):
    # mainmarks=y/x*stmarks