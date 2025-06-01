import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

def load_labeled_documents(folder_path):
    documents = []
    labels = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            label = filename.split("_")[0]  # 'education_1.txt' → 'education'
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                documents.append(f.read())
                labels.append(label)
    
    return documents, labels

def train_and_classify(docs, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(docs)
    y = labels

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = MultinomialNB()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\n✅ Classification Report:\n")
    print(classification_report(y_test, predictions))
    print("🎯 Accuracy:", round(accuracy_score(y_test, predictions), 3))

if __name__ == "__main__":
    docs, labels = load_labeled_documents("datasets/labeled_corpus")
    train_and_classify(docs, labels)
