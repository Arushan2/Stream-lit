import streamlit as st
import pandas as pd

# Initialize the DataFrame outside of the main loop
if 'results_df' not in st.session_state:
    st.session_state.results_df = pd.DataFrame(columns=['Name', 'Calculated Marks'])

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
    # Append the result to the DataFrame
    st.session_state.results_df.loc[len(st.session_state.results_df)] = [name, calculated_marks]
    # Display the DataFrame
    st.write(st.session_state.results_df)
else:
    st.write("Enter the details and press 'Calculate Marks' to see the result.")

# Function to convert DataFrame to JSON for download
def convert_df_to_json(df):
    return df.to_json(orient='records').encode('utf-8')

# Function to convert DataFrame to CSV for download
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# Download buttons
if len(st.session_state.results_df) > 0:
    # Download button for the table as JSON
    json_data = convert_df_to_json(st.session_state.results_df)
    st.download_button(label="Download Results as JSON", data=json_data, file_name='calculated_marks.json', mime='application/json')

    # Download button for the table as CSV
    csv = convert_df_to_csv(st.session_state.results_df)
    st.download_button(label="Download Results as CSV", data=csv, file_name='calculated_marks.csv', mime='text/csv')

# Print button for the table
print_button = st.button("Print Table")
if print_button:
    st.write(st.session_state.results_df)
