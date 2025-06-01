import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def create_wordcloud(tfidf_path, output_folder="datasets/tfidf_results/wordclouds"):
    df = pd.read_csv(tfidf_path, index_col=0)
    df.fillna(0, inplace=True)

    import os
    os.makedirs(output_folder, exist_ok=True)

    for doc_name in df.index:
        word_scores = df.loc[doc_name].to_dict()
        wordcloud = WordCloud(font_path='NotoNaskhArabic-Regular.ttf',  # A font that supports Pashto
                              width=800, height=400, background_color='white').generate_from_frequencies(word_scores)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title(f"📄 {doc_name}")
        save_path = os.path.join(output_folder, f"{doc_name}_wordcloud.png")
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
        print(f"✅ Word cloud saved: {save_path}")

if __name__ == "__main__":
    create_wordcloud("datasets/tfidf_results/tfidf_output.csv")
