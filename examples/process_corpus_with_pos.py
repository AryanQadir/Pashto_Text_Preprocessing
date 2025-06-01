import os
import sys

# Add root project folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pashto_nlp.normalization import normalize_text
from pashto_nlp.tokenization import tokenize
from pashto_nlp.stopwords import load_stopwords, remove_stopwords
from pashto_nlp.stemming import stem_tokens
from pashto_nlp.pos_tagger import rule_based_pos_tag

def load_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return sorted({line.strip() for line in f if line.strip()}, key=len, reverse=True)

# Load resources
stopwords = set(load_list('resources/stopwords.txt'))
prefixes = load_list('resources/prefixes.txt')
suffixes = load_list('resources/suffixes.txt')

# Define folders
raw_folder = 'datasets/raw_corpus'
cleaned_folder = 'datasets/cleaned_corpus'
pos_folder = 'results/pos_corpus'

# Create output folders if not exist
os.makedirs(cleaned_folder, exist_ok=True)
os.makedirs(pos_folder, exist_ok=True)

# Process files
for filename in os.listdir(raw_folder):
    if filename.endswith('.txt'):
        print(f"🔄 Processing: {filename}")
        with open(os.path.join(raw_folder, filename), 'r', encoding='utf-8') as f:
            raw_text = f.read()

        normalized = normalize_text(raw_text)
        tokens = tokenize(normalized)
        filtered = remove_stopwords(tokens, stopwords)
        stemmed = stem_tokens(filtered)

        # Save cleaned tokens
        with open(os.path.join(cleaned_folder, filename), 'w', encoding='utf-8') as out_clean:
            out_clean.write(' '.join(stemmed))

        # Save POS tags
        pos_tags = rule_based_pos_tag(filtered)
        with open(os.path.join(pos_folder, filename.replace('.txt', '_pos.txt')), 'w', encoding='utf-8') as out_pos:
            for token, tag in pos_tags:
                out_pos.write(f"{token}\t{tag}\n")

print("✅ All files processed. Cleaned and POS-tagged output saved.")
