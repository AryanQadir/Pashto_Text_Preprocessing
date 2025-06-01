import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Set paths
input_folder = "datasets/cleaned_corpus"
output_csv = "datasets/tfidf_results/tfidf_output.csv"

# Step 2: Load cleaned Pashto files
documents = []
filenames = []

for file in os.listdir(input_folder):
    if file.endswith(".txt"):
        with open(os.path.join(input_folder, file), "r", encoding="utf-8") as f:
            content = f.read()
            documents.append(content)
            filenames.append(file)

# Step 3: Apply TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()

# Step 4: Build rows
rows = []
for doc_index, doc_name in enumerate(filenames):
    row = tfidf_matrix[doc_index].toarray()[0]
    for i, score in enumerate(row):
        if score > 0:
            rows.append({
                "document": doc_name,
                "keyword": feature_names[i],
                "score": score
            })

# Step 5: Save to CSV (with header!)
os.makedirs(os.path.dirname(output_csv), exist_ok=True)
df = pd.DataFrame(rows)
df.to_csv(output_csv, index=False, encoding="utf-8")

print(f"✅ TF-IDF output saved to: {output_csv}")
