"""
Pashto Stemmer Module

Provides a simple rule-based stemmer for Pashto language.
Removes common suffixes and prefixes to extract root words.
"""
from pashto_nlp.stem_roots_en_ps import ROOT_MAPPINGS

def stem_with_roots(token):
    return ROOT_MAPPINGS.get(token, token)

from typing import List

# Common Pashto suffixes for stemming (no duplicates, sorted longest first)
COMMON_SUFFIXES = [
    'وونه', 'ونه', 'ګانې', 'ګانو', 'انو', 'ونه',  # plurals and derivations
    'و', 'ې', 'ي',  # common endings
]

# Common Pashto prefixes that can be stripped in stemming (optional)
COMMON_PREFIXES = [
    'بې', 'نا', 'له', 'په', 'پر', 'د',  # examples of prefixes
]

# Optional dictionary mapping some irregular or root forms
ROOT_WORDS_DICT = {
    # 'کالونه': 'کال', # example mapping if you want to override
}


def pashto_stem(word: str) -> str:
    """
    Stem a single Pashto word by removing common prefixes and suffixes.

    Args:
        word (str): The input Pashto word.

    Returns:
        str: The stemmed/root word.
    """
    if not word or len(word) < 3:
        return word

    # Check if word is in root dictionary (irregular cases)
    if word in ROOT_WORDS_DICT:
        return ROOT_WORDS_DICT[word]

    # Remove suffixes
    for suffix in sorted(set(COMMON_SUFFIXES), key=len, reverse=True):
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            word = word[:-len(suffix)]
            break  # only remove one suffix

    # Remove prefixes
    for prefix in sorted(set(COMMON_PREFIXES), key=len, reverse=True):
        if word.startswith(prefix) and len(word) > len(prefix) + 2:
            word = word[len(prefix):]
            break  # only remove one prefix

    return word


def stem_tokens(tokens: List[str]) -> List[str]:
    """
    Apply stemming to a list of Pashto tokens.

    Args:
        tokens (List[str]): List of Pashto tokens.

    Returns:
        List[str]: List of stemmed tokens.
    """
    return [pashto_stem(token) for token in tokens]


if __name__ == "__main__":
    # Simple test examples
    sample_words = [
        'کتابونه', 'ښوونځي', 'ماشومانو', 'بېوزله', 'ناسمه', 'پرهار', 'کورونه', 'زیاتې', 'ښایسته'
    ]
    print("Original -> Stemmed")
    for w in sample_words:
        print(f"{w} -> {pashto_stem(w)}")
