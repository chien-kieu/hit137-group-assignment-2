"""
TASK_1
Extract the ‘text’ in all the CSV files and store them into a single ‘.txt file’.
"""
import pandas as pd
import glob

PATH = '/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment 2'
# Path to the directory containing CSV files
csv_files_path = "/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2/*.csv"

# Path to the output text file
output_txt_file = "/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2/text_files/"

# List to store text data from all CSV files
text_data = []

# Iterate through each CSV file in the directory
for file_path in glob.glob(csv_files_path):
    # Read the CSV file using pandas
    df = pd.read_csv(file_path)
    
    # Assuming 'text' is a column name in the CSV, adjust accordingly
    if 'text' in df.columns:
        # Extract text from the 'text' column and append to the list
        text_data.extend(df['text'].astype(str).tolist())

# Write the extracted text data to the output text file
with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
    for text_line in text_data:
        txt_file.write(text_line + '\n')

print(f'Text data from CSV files has been extracted and stored in {output_txt_file}')
