import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load TF-IDF results
file_path = "datasets/tfidf_results/tfidf_output.csv"

if not os.path.exists(file_path):
    print("❌ tfidf_output.csv not found!")
    exit()

df = pd.read_csv(file_path)

# 🔁 Print available documents for reference
print("\nAvailable documents:")
print(df["document"].unique())

# 🔄 Automatically pick the first document or ask user
doc_name = df["document"].unique()[0]  # You can change this to a specific file if needed

# Filter for the selected document
keywords = df[df["document"] == doc_name].sort_values(by="score", ascending=False).head(20)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x="score", y="keyword", data=keywords, palette="viridis")
plt.title(f"Top Keywords for: {doc_name}")
plt.xlabel("TF-IDF Score")
plt.ylabel("Keyword")
plt.tight_layout()

# Save figure
output_image_path = f"datasets/tfidf_results/keywords_bar_{doc_name.replace('.txt','')}.png"
plt.savefig(output_image_path)
plt.show()

print(f"\n✅ Bar chart saved to: {output_image_path}")
