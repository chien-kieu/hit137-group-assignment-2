"""
QUESTION 1 Task 4

Link to git: https://github.com/chien-kieu/hit137-group-assignment-2/edit/main/question_1_task_4.py
"""
import spacy
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline
import csv

def extract_entities_from_spacy(text, spacy_model, entity_type):
    doc = spacy_model(text)
    entities = [ent.text for ent in doc.ents if ent.label_ == entity_type]
    return entities

def extract_entities_from_biobert(text, model_name, entity_type):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)
    
    # Use the pipeline to identify entities in the text
    ner_results = ner_pipeline(text)
    
    # Extract entities of the specified type
    entities = [result['word'] for result in ner_results if result["entity"] == entity_type]
    
    return entities

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def process_text_spacy(text, nlp):
    doc_spacy = nlp(text)
    diseases_spacy = [ent.text for ent in doc_spacy.ents if ent.label_ == 'DISEASE']
    drugs_spacy = [ent.text for ent in doc_spacy.ents if ent.label_ == 'CHEMICAL']
    return diseases_spacy, drugs_spacy

def compare_entities(entity_set1, entity_set2):
    common_entities = set(entity_set1) & set(entity_set2)
    differences = set(entity_set1) - set(entity_set2)
    return len(entity_set1), len(entity_set2), common_entities, differences

# Load the spaCy model for biomedical entities
nlp_spacy = spacy.load('en_ner_bc5cdr_md')

# Specify the path to your text file
file_path = "combined_text.txt"

# Specify the path for the CSV file
csv_file_path = "output.csv"

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header to CSV file
    csv_writer.writerow(['Total Diseases (SpaCy)', 'Total Diseases (BioBERT)',
                            'Common Diseases', 'Differences in Diseases',
                            'Total Drugs (SpaCy)', 'Total Drugs (BioBERT)',
                            'Common Drugs', 'Differences in Drugs'])

    # Read the text from the file in chunks
    chunk_size = 1000000
    all_results = []

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            # Process text with SpaCy
            diseases_spacy, drugs_spacy = process_text_spacy(chunk, nlp_spacy)

            # Process text with BioBERT
            diseases_biobert = extract_entities_from_biobert(chunk, "ugaray96/biobert_ncbi_disease_ner", "Disease")
            drugs_biobert = extract_entities_from_biobert(chunk, "alvaroalon2/biobert_chemical_ner", "Chemical")

            # Compare entities detected by SpaCy and BioBERT
            total_diseases_spacy, total_diseases_biobert, common_diseases, diff_diseases = compare_entities(
                diseases_spacy, diseases_biobert
            )

            total_drugs_spacy, total_drugs_biobert, common_drugs, diff_drugs = compare_entities(
                drugs_spacy, drugs_biobert
            )

            # Save results for the current chunk
            all_results = [total_diseases_spacy, total_diseases_biobert,
                            common_diseases, diff_diseases,
                            total_drugs_spacy, total_drugs_biobert,
                            common_drugs, diff_drugs]

    # Write final results to CSV file
    csv_writer.writerow(all_results)

print(f"\nThe final comparison results have been saved to {csv_file_path}")
