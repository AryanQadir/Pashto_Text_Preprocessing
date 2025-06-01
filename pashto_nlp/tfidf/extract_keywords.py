import pandas as pd

def extract_top_keywords(csv_path, top_n=10):
    df = pd.read_csv(csv_path, index_col=0)

    for doc_name in df.index:
        row = df.loc[doc_name]
        top_keywords = row.sort_values(ascending=False).head(top_n)
        print(f"\n🔑 Top {top_n} keywords in {doc_name}:")
        for word, score in top_keywords.items():
            print(f"{word}: {round(score, 3)}")

if __name__ == "__main__":
    extract_top_keywords("datasets/tfidf_results/tfidf_output.csv", top_n=10)
