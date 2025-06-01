import re

def tokenize(text):
    """
    Tokenizes Pashto text into words using whitespace and punctuation splitting.
    """
    # Normalize spaces and remove unwanted characters
    text = re.sub(r"[؟،؛!«»\"\[\](){}<>]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenize by spaces
    tokens = text.split()
    return tokens
