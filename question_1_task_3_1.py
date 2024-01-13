import re
import pandas as pd
from collections import Counter

def analyze_and_save_top_30_words(file_path):
    # Read content from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Use regular expression to extract words
    words = re.findall(r'\b\w+\b', text)

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Get the top 30 words and their counts
    top_30_words = [(word, count) for word, count in word_counts.most_common(30)]

    # Save the top 30 words and their counts to a CSV file
    df_top_30 = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
    output_csv_file = 'top_30_words.csv'
    df_top_30.to_csv(output_csv_file, index=False)

    print(f"The top 30 words and their counts have been saved to {output_csv_file}")

def main():
    input_file_path = 'combined_text.txt'
    analyze_and_save_top_30_words(input_file_path)

if __name__ == "__main__":
    main()
