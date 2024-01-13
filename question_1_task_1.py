import csv
import os

def extract_words_from_csv(csv_file_path):
    extracted_words = []
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        # next(csv_reader)  # Skip the header row
        for row in csv_reader:
            for cell in row:
                extracted_words.extend(cell.split())  # Split each cell into words
    return extracted_words

def save_words_to_text_file(words_list, output_text_path):
    with open(output_text_path, 'w', encoding='utf-8') as txtfile:
        for word in words_list:
            txtfile.write(word + '\n')

def process_csv_files_and_save_text(csv_folder_path, output_text_path):
    all_extracted_words = []

    # Loop through all files in the specified folder
    for filename in os.listdir(csv_folder_path):
        if filename.endswith(".csv"):
            csv_file_path = os.path.join(csv_folder_path, filename)
            extracted_words = extract_words_from_csv(csv_file_path)
            all_extracted_words.extend(extracted_words)

    # Save all extracted words to a single text file
    save_words_to_text_file(all_extracted_words, output_text_path)
    print("Words from CSV files have been saved to", output_text_path)

def main():
    csv_folder_path = os.getcwd()
    # Create path for text file
    output_text_path = os.path.join(csv_folder_path,'combined_text.txt')

    # TASK 1: Extract the ‘text’ in all the CSV files and store them into combined_text.txt file
    process_csv_files_and_save_text(csv_folder_path, output_text_path)

if __name__ == "__main__":
    main()