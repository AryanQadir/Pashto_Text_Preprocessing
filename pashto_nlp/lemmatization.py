# lemmatization.py

# ✅ Expanded dictionary of common Pashto lemmas
pashto_lemma_dict = {
    "کتابونه": "کتاب",
    "کتابونو": "کتاب",
    "ښوونځي": "ښوونځی",
    "زده‌کوونکي": "زده‌کوونکی",
    "زده کوونکي": "زده‌کوونکی",
    "ښوونکي": "ښوونکی",
    "ښوونکې": "ښوونکی",
    "تللې": "تلل",
    "تللی": "تلل",
    "کړې": "کول",
    "کړی": "کول",
    "کړي": "کول",
    "ليکلې": "ليکل",
    "ليکل": "ليکل",
    "ليکم": "ليکل",
    "ويلې": "ويل",
    "وايي": "ويل",
    "ويل": "ويل",
    "کوي": "کول",
    "کړي": "کول"
}

# ✅ Optional suffix-based fallback
lemma_suffixes = ["ونه", "ونو", "و", "ې", "ی", "یې", "ېې", "یانو", "ګان", "ان", "ون", "ي", "یو", "ې"]

def strip_suffix_fallback(token):
    """
    Removes known Pashto suffixes to attempt basic lemma fallback.
    """
    for suffix in sorted(lemma_suffixes, key=len, reverse=True):
        if token.endswith(suffix) and len(token) > len(suffix) + 1:
            return token[:-len(suffix)]
    return token

def lemmatize_token(token):
    """
    Returns the lemma from dictionary or applies suffix-stripping fallback.
    """
    if token in pashto_lemma_dict:
        return pashto_lemma_dict[token]
    return strip_suffix_fallback(token)

def lemmatize_tokens(tokens):
    """
    Applies lemmatization to a list of tokens.
    """
    return [lemmatize_token(token) for token in tokens]
