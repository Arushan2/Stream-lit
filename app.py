import streamlit as st

# Inputs for the total marks in sub and main schemes, and the student's name and marks
x = st.number_input("Insert total marks as your sub scheme", value=0)
y = st.number_input("Insert total marks as your main scheme", value=0)
name = st.text_input("Enter your Name")
stmarks = st.number_input("Insert student's marks", value=0)

# Function to calculate marks based on the schemes
def calculate(sub_scheme, main_scheme, student_marks):
    if sub_scheme != 0:  # Prevent division by zero
        mainmarks = main_scheme / sub_scheme * student_marks
        return mainmarks
    else:
        return 0

# Call the function and display the result
calculated_marks = calculate(x, y, stmarks)
st.write(f"{name}'s calculated marks: {calculated_marks}")


