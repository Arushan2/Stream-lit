import streamlit as st
import pandas as pd
from io import BytesIO

# Inputs for the total marks in sub and main schemes, and the student's name and marks
x = st.number_input("Insert total marks as your sub scheme", min_value=0, step=1, format='%d')
y = st.number_input("Insert total marks as your main scheme", min_value=0, step=1, format='%d')
name = st.text_input("Enter your Name")
stmarks = st.number_input("Insert student's marks", min_value=0, step=1, format='%d')

# Function to calculate marks based on the schemes
def calculate(sub_scheme, main_scheme, student_marks):
    if sub_scheme != 0:  # Prevent division by zero
        mainmarks = main_scheme / sub_scheme * student_marks
        return mainmarks
    else:
        return 0

# Check if all inputs are provided
all_inputs_provided = x > 0 and y > 0 and name and stmarks >= 0

# Function to write data to a file and return a file-like object
def to_excel(name, marks):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        pd.DataFrame({'Name': [name], 'Marks': [marks]}).to_excel(writer, index=False, sheet_name='Marks')
    output.seek(0)
    return output

# Button to trigger the calculation and file download
if all_inputs_provided:
    if st.button('Calculate Marks'):
        calculated_marks = calculate(x, y, stmarks)
        st.write(f"{name}'s calculated marks: {calculated_marks}")

        # Create an excel file and download button
        file = to_excel(name, calculated_marks)
        st.download_button(
            label="Download Marks File",
            data=file,
            file_name="student_marks.xlsx",
            mime="application/vnd.ms-excel"
        )
else:
    st.write("Please enter all required fields to enable the calculation.")
