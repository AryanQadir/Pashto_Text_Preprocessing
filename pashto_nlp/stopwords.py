# pashto_nlp/stopwords.py

def load_stopwords(filepath='resources/stopwords.txt'):
    stopword_set = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            if word:
                stopword_set.add(word)
    return stopword_set


def remove_stopwords(tokens, stopwords):
    return [token for token in tokens if token not in stopwords]
