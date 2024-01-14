"""
QUESTION 1 Task 1

Link to git: https://github.com/chien-kieu/hit137-group-assignment-2/blob/main/question_1_task_1.py
"""
import zipfile
import pandas as pd

zip_file_path = 'Assignment 2.zip'
output_txt_file = 'combined_text.txt'
all_texts = []

# Extract CSV files from the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Get a list of CSV file names in the zip file
    csv_files = [name for name in zip_ref.namelist() if name.endswith('.csv')]

    # Iterate through each CSV file in the zip file
    for csv_file in csv_files:
        # Read the CSV file using pandas
        df = pd.read_csv(zip_ref.open(csv_file))

        # Check if the DataFrame has any data
        if not df.empty:
            # Concatenate all text from all columns in the DataFrame
            text = '\n'.join(df.astype(str).agg(' '.join, axis=1))
            all_texts.append(text)
        else:
            print(f"Warning: {csv_file} is empty. Skipping.")

# Combine all texts into a single string
combined_text = '\n'.join(all_texts)

# Save the combined text to a .txt file
with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
    txt_file.write(combined_text)

print(f"Combined text has been saved to '{output_txt_file}'.")
