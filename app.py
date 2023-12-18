import streamlit as st
import json

# Initialize a list to store student data
students_data = []

x = st.number_input("Insert total marks as your sub scheme", value=None)
y = st.number_input("Insert total marks as your main scheme", value=None)

def calculate(sub_scheme, main_scheme, student_marks):
    if sub_scheme != 0: 
        mainmarks = main_scheme / sub_scheme * student_marks
        return mainmarks
    else:
        return 0

# Form for inputting student data
with st.form("student_data_form"):
    name = st.text_input("Enter your Name")
    stmarks = st.number_input("Insert student's marks", value=None)
    submitted = st.form_submit_button("Add Student")

# Adding student data to the list
if submitted:
    calculated_marks = calculate(x, y, stmarks)
    students_data.append({"Name": name, "Marks": calculated_marks})
    st.write(f"{name}'s calculated marks: {calculated_marks}")

# Button to download data as JSON
if st.button('Download Data as JSON'):
    # Convert student data to JSON
    json_data = json.dumps(students_data, indent=4)
    # Create a download button
    st.download_button(label='Download JSON',
                       data=json_data,
                       file_name='students_data.json',
                       mime='application/json')

# Display message if the list is empty
if not students_data:
    st.write("Add students and calculate their marks to download the data.")
