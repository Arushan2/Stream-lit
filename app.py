import streamlit as st
import json

# Function to calculate marks
def calculate(sub_scheme, main_scheme, student_marks):
    if sub_scheme != 0: 
        mainmarks = main_scheme / sub_scheme * student_marks
        return mainmarks
    else:
        return 0

# Store student data
student_data = []

# Input fields
x = st.number_input("Insert total marks as your sub scheme", value=None)
y = st.number_input("Insert total marks as your main scheme", value=None)
name = st.text_input("Enter your Name")
stmarks = st.number_input("Insert student's marks", value=None)

# Button to calculate marks
if st.button('Calculate Marks'):
    calculated_marks = calculate(x, y, stmarks)
    st.write(f"{name}'s calculated marks: {calculated_marks}")
    # Add student data to the list
    student_data.append({"Name": name, "Marks": calculated_marks})
else:
    st.write("Enter the details and press 'Calculate Marks' to see the result.")

# Function to download data as JSON
def download_json(data):
    json_data = json.dumps(data)
    st.download_button(
        label="Download Data as JSON",
        data=json_data,
        file_name='student_data.json',
        mime='application/json'
    )

# Show download button
if student_data:
    download_json(student_data)
