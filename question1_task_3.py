"""
TASK_3
Count the occurrences of the words in the text (.txt) and give the ‘Top 30’ most common words.
And store the ‘Top 30’ common words and their counts into a CSV file.
"""
import re
import csv
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Read the file and convert text to lowercase
        words = re.findall(r'\b\w+\b', text)  # Use regular expression to extract words

    word_counts = Counter(words)
    return word_counts

def save_top30_to_csv(word_counts, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Word', 'Count'])

        for word, count in word_counts.most_common(30):
            csv_writer.writerow([word, count])

if __name__ == "__main__":
    # Replace 'your_file.txt' and 'output.csv' with your actual file names
    input_file_path = '/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2/combined_text.txt'
    output_csv_path = '/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2/output.csv'

    word_counts = count_words(input_file_path)
    save_top30_to_csv(word_counts, output_csv_path)

    print("Top 30 words and their counts have been saved to", output_csv_path)