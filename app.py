import streamlit as st

# Input fields for total marks, student's name, and student's marks
x = st.number_input("Insert total marks as your sub scheme", value=None)
y = st.number_input("Insert total marks as your main scheme", value=None)
name = st.text_input("Enter your Name")
stmarks = st.number_input("Insert student's marks", value=None)
download_button=st.download_button(label="Download Marks")
# Function to calculate the main marks based on the sub scheme, main scheme, and student's marks
def calculate(sub_scheme, main_scheme, student_marks):
    if sub_scheme != 0: 
        mainmarks = main_scheme / sub_scheme * student_marks
        return mainmarks
    else:
        return 0

# Button to calculate and display the marks
if st.button('Calculate Marks'):
    calculated_marks = calculate(x, y, stmarks)
    st.write(f"{name}'s calculated marks: {calculated_marks}")

    # Preparing the text to download
    download_text = f"Name: {name}\nCalculated Marks: {calculated_marks}"

    # Creating a download button for the text
    download_button(label="Download Marks", data=download_text, file_name=f"{name}_marks.txt", mime="text/plain")

else:
    st.write("Enter the details and press 'Calculate Marks' to see the result.")
