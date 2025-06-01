def rule_based_pos_tag(tokens):
    """
    A rule-based POS tagger for Pashto tokens.
    Returns a list of (token, POS) pairs.
    """

    # Extended Pashto lexicon
    lexicon = {
        "زه": "PRON", "ته": "PRON", "دی": "PRON", "ده": "PRON", "تاسو": "PRON", "موږ": "PRON",
        "کتاب": "NOUN", "کتابونه": "NOUN", "ښوونځی": "NOUN", "زده کوونکی": "NOUN", "ښوونکی": "NOUN", "ماشوم": "NOUN",
        "ښکلی": "ADJ", "خوښ": "ADJ", "ښه": "ADJ", "تکړه": "ADJ", "غټ": "ADJ",
        "ځم": "VERB", "وینم": "VERB", "کوم": "VERB", "خورم": "VERB", "وړم": "VERB", "لولم": "VERB",
        "په": "PREP", "له": "PREP", "د": "PREP", "تر": "PREP",
        "او": "CONJ", "خو": "CONJ", "یا": "CONJ",
        "نه": "ADV", "بیا": "ADV", "هم": "ADV", "ډېر": "ADV",
        "یو": "DET", "یوه": "DET", "دا": "DET", "هغه": "DET",
        "څوک": "INT", "څه": "INT", "ولې": "INT", "څنګه": "INT"
    }

    # Suffix-based heuristic rules
    suffix_rules = {
        "ونه": "NOUN", "ان": "NOUN", "ګان": "NOUN",
        "یدل": "VERB", "ېدل": "VERB", "ول": "VERB", "دل": "VERB",
        "ونکی": "NOUN", "ېدونکی": "ADJ",
        "يز": "ADJ", "ی": "ADJ",
        "ه": "PRON", "و": "VERB"
    }

    tagged = []

    for token in tokens:
        pos = lexicon.get(token)

        if not pos:
            for suffix, tag in suffix_rules.items():
                if token.endswith(suffix):
                    pos = tag
                    break

        if not pos:
            pos = "X"  # Unknown

        tagged.append((token, pos))

    return tagged

# Example usage
if __name__ == "__main__":
    sentence = "زه ښوونځي ته ځم او کتابونه لولم"
    tokens = sentence.split()
    tagged = rule_based_pos_tag(tokens)
    for token, pos in tagged:
        print(f"{token}\t{pos}")
