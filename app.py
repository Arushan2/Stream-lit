import streamlit as st
import pandas as pd

# Initialize the DataFrame outside of the main loop
if 'results_df' not in st.session_state:
    st.session_state.results_df = pd.DataFrame(columns=['Name', 'Calculated Marks'])

x = st.number_input("Insert total marks as your sub scheme", value=0)
y = st.number_input("Insert total marks as your main scheme", value=0)

# Use session state to store and update the name and student marks
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'student_marks' not in st.session_state:
    st.session_state.student_marks = 0

name = st.text_input("Enter your Name", value=st.session_state.name)
stmarks = st.number_input("Insert student's marks", value=st.session_state.student_marks)

def calculate(sub_scheme, main_scheme, student_marks):
    if sub_scheme != 0: 
        mainmarks = main_scheme / sub_scheme * student_marks
        return mainmarks
    else:
        return 0

if st.button('Calculate Marks'):
    calculated_marks = calculate(x, y, stmarks)
    st.write(f"{name}'s calculated marks: {calculated_marks}")
    # Append the result to the DataFrame
    st.session_state.results_df.loc[len(st.session_state.results_df)] = [name, calculated_marks]
    # Display the DataFrame
    st.write(st.session_state.results_df)

    # Clear the name and student marks fields after calculation
    st.session_state.name = ""
    st.session_state.student_marks = 0

    # Rerun the app to reflect changes
    st.experimental_rerun()
else:
    st.write("Enter the details and press 'Calculate Marks' to see the result.")

# Remaining code for download buttons and print button
# ...
