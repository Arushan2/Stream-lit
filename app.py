import streamlit as st
x = st.number_input("Insert total marks as your sub scheme", value=None)
y = st.number_input("Insert total marks as your main scheme", value=None)
name = st.text_input("Enter your Name")
stmarks = st.number_input("Insert student's marks", value=None)
def calculate(sub_scheme, main_scheme, student_marks):
    if sub_scheme != 0: 
        mainmarks = main_scheme / sub_scheme * student_marks
        return mainmarks
    else:
        return 0
if st.button('Calculate Marks'):
    calculated_marks = calculate(x, y, stmarks)
    st.write(f"{name}'s calculated marks: {calculated_marks}")
else:
    st.write("Enter the details and press 'Calculate Marks' to see the result.")