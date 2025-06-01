# examples/full_pipeline_with_pos.py

import os
import sys

# Add root package to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pashto_nlp.normalization import normalize_text
from pashto_nlp.tokenization import tokenize
from pashto_nlp.stopwords import load_stopwords, remove_stopwords
from pashto_nlp.stemming import stem_tokens
from pashto_nlp.pos_tagger import rule_based_pos_tag

# Example sentence
text = "زه ښوونځي ته ځم او کتابونه لولم او دیموکراتان خبرې کوي"

# Step 1: Normalize
normalized = normalize_text(text)

# Step 2: Tokenize
tokens = tokenize(normalized)

# Step 3: Remove Stopwords
stopwords = load_stopwords("resources/stopwords.txt") 
filtered = remove_stopwords(tokens, stopwords)
# Step 4: Stem (dictionary + affix-based)
stemmed = stem_tokens(filtered)

# Step 5: POS Tagging
pos_tags = rule_based_pos_tag(filtered)

# Output all steps
print("Original Text:", text)
print("Normalized:", normalized)
print("Tokens:", tokens)
print("Filtered (Stopwords Removed):", filtered)
print("Stemmed:", stemmed)
print("\nPOS Tags:")
for token, tag in pos_tags:
    print(f"{token}\t→\t{tag}")
