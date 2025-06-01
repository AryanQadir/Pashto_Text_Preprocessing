import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_documents(folder_path):
    documents = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                documents.append(f.read())
                filenames.append(filename)
    return documents, filenames

def search_query(query, documents, filenames):
    # Add query to the list of documents
    all_texts = documents + [query]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # Compare query (last row) to all documents
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    ranked_indices = np.argsort(similarity_scores)[::-1]
    print(f"\n🔍 Query: {query}\n")
    print("📄 Top matching documents:")
    for idx in ranked_indices[:5]:
        print(f"{filenames[idx]} — Similarity: {round(similarity_scores[idx], 3)}")

if __name__ == "__main__":
    docs, names = load_documents("datasets/cleaned_corpus")

    print("🔎 Enter your Pashto search query:")
    user_query = input(">> ")
    
    search_query(user_query, docs, names)
