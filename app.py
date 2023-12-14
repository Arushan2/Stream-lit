import streamlit as st
st.write("Vanakkkam ulaham ")
def calculate(a,b,c):
    x=(-b+(b**2-4*a*c)**1/2)/2*a
    return x
userinputa=st.number_input('Insert a number a')
userinputb=st.number_input('Insert a number b')
userinputc=st.number_input('Insert a number c')
st.write(calculate(userinputa,userinputb,userinputc))




