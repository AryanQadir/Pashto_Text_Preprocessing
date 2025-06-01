# This script generates a simulated POS-tagged Pashto file for testing

import os

# Sample Pashto words with fake POS tags for demonstration
sample_data = [
    ('کتاب', 'NOUN'),
    ('لولي', 'VERB'),
    ('ښه', 'ADJ'),
    ('دی', 'PRON'),
    ('زه', 'PRON'),
    ('ورته', 'ADV'),
    ('یو', 'NUM'),
    ('کور', 'NOUN'),
    ('جوړ', 'ADJ'),
    ('کړی', 'VERB'),
    ('باندې', 'ADP'),
    ('خوښ', 'ADJ'),
    ('وو', 'VERB'),
    ('موږ', 'PRON')
]

# Ensure output folder exists
os.makedirs('datasets/cleaned_corpus', exist_ok=True)

# Save simulated POS-tagged file
output_path = 'datasets/cleaned_corpus/cleaned_pos_corpus.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    for word, tag in sample_data:
        f.write(f"{word}\t{tag}\n")

print(f"Simulated POS file saved to: {output_path}")
