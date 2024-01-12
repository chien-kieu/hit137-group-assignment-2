# """
# TASK_1
# Extract the ‘text’ in all the CSV files and store them into a single ‘.txt file’.
# """
# import csv
# import os

# def extract_words_from_csv(csv_file_path):
#     words = []
#     with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
#         csv_reader = csv.reader(csvfile)
#         # next(csv_reader)  # Skip the header row
#         for row in csv_reader:
#             for cell in row:
#                 words.extend(cell.split())  # Split each cell into words
#     return words

# def save_to_text_file(all_words, output_text_path):
#     with open(output_text_path, 'w', encoding='utf-8') as txtfile:
#         for word in all_words:
#             txtfile.write(word + '\n')

# if __name__ == "__main__":
#     # Replace 'path_to_folder_containing_csv_files' with the folder containing your CSV files
#     csv_folder = '/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2'
#     output_text_path = '/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2/combined_text.txt'

#     all_words = []

#     # Loop through all files in the specified folder
#     for filename in os.listdir(csv_folder):
#         if filename.endswith(".csv"):
#             csv_file_path = os.path.join(csv_folder, filename)
#             words = extract_words_from_csv(csv_file_path)
#             all_words.extend(words)

#     # Save all extracted words to a single text file
#     save_to_text_file(all_words, output_text_path)

#     print("Words from CSV files have been saved to", output_text_path)

from transformers import BertTokenizer
from collections import Counter

def count_unique_tokens(file_path, model_name):
    # Load the tokenizer
    tokenizer = BertTokenizer.from_pretrained(model_name)

    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count the occurrences of each token
    token_counts = Counter(tokens)

    # Return the top 30 tokens
    top30_tokens = token_counts.most_common(30)
    return top30_tokens

if __name__ == "__main__":
    # Replace 'your_file.txt' with the path to your text file
    input_file_path = '/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2/combined_text.txt'
    
    # Replace 'bert-base-uncased' with the desired pre-trained model name
    model_name = 'bert-base-uncased'

    top30_tokens = count_unique_tokens(input_file_path, model_name)

    print("Top 30 unique tokens and their counts:")
    for token, count in top30_tokens:
        print(f"{token}: {count}")