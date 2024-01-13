import re
import pandas as pd
from collections import Counter

output_csv_file = 'top_30_words.csv'

# Read content from the file
with open('combined_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Use regular expression to extract words
words = re.findall(r'\b\w+\b', text)

# Count the occurrences of each word
word_counts = Counter(words)

# Count the top 30 words
top_30_words = word_counts.most_common(30)

# Save the top 30 words and their counts to a CSV file
df_top_30 = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
df_top_30.to_csv(output_csv_file, index=False)

print(f"The top 30 words and their counts have been saved to {output_csv_file}")