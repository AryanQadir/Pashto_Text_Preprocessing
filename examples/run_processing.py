import os
import re

# Define reusable function 
def run_full_pipeline(raw_folder, cleaned_folder, stopword_path, prefix_path, suffix_path, chunk_size=100):
    def load_list(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return sorted({line.strip() for line in f if line.strip()}, key=len, reverse=True)

    def normalize(text):
        text = text.lower()
        text = text.replace('ك', 'ک').replace('ي', 'ی').replace('ۀ', 'ه')
        text = re.sub(r'[^\u0600-\u06FF\s]', '', text)
        return re.sub(r'\s+', ' ', text).strip()

    def tokenize(text):
        return text.split()

    def remove_stopwords(tokens, stopwords):
        return [t for t in tokens if t not in stopwords]

    def strip_affixes(token, prefixes, suffixes):
        for prefix in prefixes:
            if token.startswith(prefix) and len(token) > len(prefix) + 1:
                token = token[len(prefix):]
                break
        for suffix in suffixes:
            if token.endswith(suffix) and len(token) > len(suffix) + 1:
                token = token[:-len(suffix)]
                break
        return token

    def stem_tokens(tokens, prefixes, suffixes):
        return [strip_affixes(token, prefixes, suffixes) for token in tokens]

    os.makedirs(cleaned_folder, exist_ok=True)
    stopwords = set(load_list(stopword_path))
    prefixes = load_list(prefix_path)
    suffixes = load_list(suffix_path)

    for filename in os.listdir(raw_folder):
        if filename.endswith('.txt'):
            print(f"🔄 Processing {filename}")
            with open(os.path.join(raw_folder, filename), 'r', encoding='utf-8') as f:
                raw_text = ''
                for line in f:
                    raw_text += line


            text = normalize(raw_text)
            tokens = tokenize(text)
            tokens = remove_stopwords(tokens, stopwords)
            tokens = stem_tokens(tokens, prefixes, suffixes)

            with open(os.path.join(cleaned_folder, filename), 'w', encoding='utf-8') as f_out:
                for i in range(0, len(tokens), chunk_size):
                    f_out.write(' '.join(tokens[i:i+chunk_size]) + '\n')

    print("✅ Preprocessing complete!")

# CLI entry point
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--chunk_size', type=int, default=100)
    args = parser.parse_args()

    run_full_pipeline(
        raw_folder='datasets/raw_corpus',
        cleaned_folder='datasets/cleaned_corpus',
        stopword_path='resources/stopwords.txt',
        prefix_path='resources/prefixes.txt',
        suffix_path='resources/suffixes.txt',
        chunk_size=args.chunk_size
    )