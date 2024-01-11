import pandas as pd

from collections import Counter
# open csv file
with open('C:/Users/musta/Downloads/all_csv_file.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()
word_counts = Counter(words)

# show 30 common words`
top_30_words = word_counts.most_common(30)

# Save Top 30 words and counts to a CSV file
df_top_30 = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
df_top_30.to_csv('top_30_words.csv', index=False)

print("Top 30 words and counts saved to top_30_words.csv")
