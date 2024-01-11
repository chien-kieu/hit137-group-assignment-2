import pandas as pd
from zipfile import ZipFile
import glob

zip_folder_path = "C:/Users/musta/Desktop/New folder.zip"

# Extract all the CSV files from the zipped folder
with ZipFile(zip_folder_path, 'r') as zip_ref:
    zip_ref.extractall("extracted_files")

# Initialize empty list to store text from all CSV files
all_texts = []

# List all CSV files in the extracted folder
csv_files = glob.glob("extracted_files/*.csv")
for csv_file in csv_files:
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file)
    texts = df['text'].astype(str).tolist()

    # Add the extracted texts to the list
    all_texts.extend(texts)

# Combine all texts into a single string
combined_text = '\n'.join(all_texts)

# Concatenate the texts into a single string
output_file_path = "C:/Users/musta/Downloads/all_csv_file.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(combined_text)

print(f"Combined text saved to {output_file_path}")