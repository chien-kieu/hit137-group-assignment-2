from transformers import AutoTokenizer
from collections import Counter
import pandas as pd

def analyze_and_save_top_30_tokens(file_path, chunk_size=1000000, top_n=30):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
    total_token_counts = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            # Tokenize the chunk
            tokens = tokenizer.tokenize(chunk)
            # Count the tokens in the chunk
            total_token_counts.update(tokens)
            
    # Get the top 30 tokens for the entire file
    top_30_tokens = total_token_counts.most_common(top_n)

    # Print the top 30 tokens for the entire file
    print(f"\nTop {top_n} tokens for the entire file:")
    for token, count in top_30_tokens:
        print(f"{token}: {count}")

    # Convert top_30_tokens to a DataFrame
    df_top_30_tokens = pd.DataFrame(top_30_tokens, columns=['Token', 'Count'])

    # Save top_30_tokens to a CSV file
    csv_file_name = f"top_{top_n}_tokens.csv"
    df_top_30_tokens.to_csv(csv_file_name, index=False)
    print(f"\nTop 30 tokens have been saved to '{csv_file_name}'.")

def main():
    input_file_path = "combined_text.txt"
    analyze_and_save_top_30_tokens(input_file_path)

if __name__ == "__main__":
    main()