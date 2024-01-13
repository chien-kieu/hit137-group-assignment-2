from transformers import BertTokenizer, BertModel, BertConfig
from collections import Counter
import pandas as pds
import concurrent.futures


def tokenize_count(tokens):
    return Counter(tokens)


def count_get_top_30words(file_path, model_name, max_sequence_length=512, top_tokens=30, batch_size=8):
    # Load this tokenizer
    tokenizer = BertTokenizer.from_pretrained(model_name, config=BertConfig.from_json_file(
        'C:/Users/musta/Downloads/BioBERT/bert_config.json'))

    # Read text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text1 = file.read()

    # Split text into chunk of max_seq_length
    chunks = [text1[i:i + max_sequence_length] for i in range(0, len(text1), max_sequence_length)]

    # Tokenize the chunks in batches
    tokenized_batches = [tokenizer.encode(chunk) for chunk in chunks]

    # Flatten the list of batches into a single list of tokens
    whole_tokens = [token for batch in tokenized_batches for token in batch]

    # Use ThreadPoolExecutor for parallel token counting
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Batch tokens for parallel processing
        token_batches = [whole_tokens[i:i + batch_size] for i in range(0, len(whole_tokens), batch_size)]

        # Submit batches to the executor for parallel processing
        futures = [executor.submit(tokenize_count, tokens) for tokens in token_batches]

        # Initialize an empty Counter for token counts
        all_token_counts = Counter()

        # Collect results as they become available
        for future in concurrent.futures.as_completed(futures):
            token_counts = future.result()
            all_token_counts += token_counts

    # Get the top N tokens
    top_30tokens = all_token_counts.most_common(top_tokens)

    # Create a DataFrame for visualization
    datafrm = pds.DataFrame(top_30tokens, columns=['Token', 'Count'])

    return datafrm


file_path = 'full_csv_file.txt'
model_path = 'C:/Users/musta/Downloads/BioBERT'

result_datafrm = count_get_top_30words(file_path, model_path)

# Show the top 30 words
print(result_datafrm)
