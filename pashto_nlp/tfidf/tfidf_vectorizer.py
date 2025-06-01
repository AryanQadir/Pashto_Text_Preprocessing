import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def load_cleaned_documents(folder_path):
    documents = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                documents.append(f.read())
                filenames.append(filename)
    return documents, filenames

def create_tfidf_matrix(documents, filenames, output_csv):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    df = pd.DataFrame(tfidf_matrix.toarray(), index=filenames, columns=vectorizer.get_feature_names_out())
    df.to_csv(output_csv, encoding='utf-8-sig')
    print(f"✅ TF-IDF saved to {output_csv}")

if __name__ == "__main__":
    docs, names = load_cleaned_documents("datasets/cleaned_corpus")
    create_tfidf_matrix(docs, names, "datasets/tfidf_results/tfidf_output.csv")
