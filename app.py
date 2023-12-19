import streamlit as st
import json
import os

# Global data list
data = []

# Input fields
x = st.number_input("Insert total marks as your sub scheme", value=0)
y = st.number_input("Insert total marks as your main scheme", value=0)
name = st.text_input("Enter your Name")
stmarks = st.number_input("Insert student's marks", value=0)

# Function to calculate marks
def calculate(sub_scheme, main_scheme, student_marks, student_name):
    if sub_scheme != 0:
        mainmarks = main_scheme / sub_scheme * student_marks
        result = {"Name": student_name, "Calculated Marks": mainmarks}
        data.append(result)
        return mainmarks
    else:
        return 0

# Function to save data to JSON file
def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4, default=str)

# Button to calculate and display marks
if st.button('Calculate Marks'):
    calculated_marks = calculate(x, y, stmarks, name)
    st.write(f"{name}'s calculated marks: {calculated_marks}")
else:
    st.write("Enter the details and press 'Calculate Marks' to see the result.")

# Button to download JSON file
json_file_path = 'calculated_marks.json'
if st.button('Download JSON Data'):
    save_data(json_file_path, data)
    with open(json_file_path, "r") as file:
        st.download_button(label="Download Data as JSON", data=file, file_name='calculated_marks.json', mime='application/json')
