import streamlit as st
import pandas as pd

x = st.number_input("Insert total marks as your sub scheme", value=None)
y = st.number_input("Insert total marks as your main scheme", value=None)
name = st.text_input("Enter your Name")
stmarks = st.number_input("Insert student's marks", value=None)

# DataFrame to store the results
results_df = pd.DataFrame(columns=['Name', 'Calculated Marks'])

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
    results_df.loc[len(results_df)] = [name, calculated_marks]
    # Display the DataFrame
    st.write(results_df)
else:
    st.write("Enter the details and press 'Calculate Marks' to see the result.")

# Function to convert DataFrame to CSV for download
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# Download button for the table as CSV
csv = convert_df_to_csv(results_df)
st.download_button(label="Download Results as CSV", data=csv, file_name='calculated_marks.csv', mime='text/csv')

# Print button for the table
print_button = st.button("Print Table")
if print_button:
    st.write(results_df)
