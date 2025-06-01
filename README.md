# Pashto Text Preprocessing Toolkit (TPTLP)

A Python toolkit for **text preprocessing in Pashto**, a low-resource and morphologically rich language.  
Includes normalization, tokenization, stopword removal, stemming, lemmatization, POS tagging, and TF-IDF support.

---

## 🚀 Features

- ✅ Unicode normalization for Pashto
- ✅ Whitespace-based tokenization
- ✅ Customizable stopword removal
- ✅ Dictionary + affix-based stemming
- ✅ Lemmatization using rule-based mapping
- ✅ Rule-based POS tagging (Pashto lexicon)
- ✅ TF-IDF keyword extraction
- ✅ Supports raw corpus and single text inputs

---

## 📦 Installation

```bash
git clone https://github.com/AryanQadir/Pashto_Text_Preprocessing
cd Pashto_Text_Preprocessing
pip install .
```

---

## 🧪 Example Usage (from `examples/full_pipeline_with_pos.py`)

```python
from pashto_nlp.normalization import normalize_text
from pashto_nlp.tokenization import tokenize
from pashto_nlp.stopwords import load_stopwords, remove_stopwords
from pashto_nlp.stemming import stem_tokens
from pashto_nlp.lemmatization import lemmatize_tokens
from pashto_nlp.pos_tagger import rule_based_pos_tag


text = "زه ښوونځي ته ځم او کتابونه لولم"
normalized = normalize_text(text)
tokens = tokenize(normalized)
stopwords = load_stopwords("resources/stopwords.txt")
filtered = remove_stopwords(tokens, stopwords)
stemmed = stem_tokens(filtered)
lemmatized = lemmatize_tokens(filtered)
tags = rule_based_pos_tag(filtered)

print("Stemmed:", stemmed)
print("Lemmatized:", lemmatized) 
print("POS Tags:", tags)
```

---

## 📂 Folder Structure

```
Pashto_Text_Preprocessing/
├── pashto_nlp/                # Processing modules
├── datasets/                  # Raw and cleaned text corpus
├── resources/                 # Stopwords, suffixes, prefixes
├── results/                   # Output files
├── tfidf/                     # TF-IDF features
├── examples/                  # Scripts (e.g., run_processing.py)
├── figures/                   # Optional visual outputs
├── paper.md                   # JOSS paper
├── README.md                  # This file
└── setup.py                   # Pip installer
```

---

## 📖 Dataset

The pipeline has been evaluated on the **Pashto Text Corpus (PTC)** containing over **50,000 documents** from books, news, and historical texts.

## Full Dataset (50,000 Pashto Documents)
Due to size limitations, the full dataset is not included in this repository.
If you would like access to the full Pashto corpus used in this research, please contact on my email aryanqadira1@gmail.com.
The sample data in `datasets/raw_corpus` can be used to test and explore the preprocessing pipeline.
---

## 📜 License

MIT License. See [`LICENSE`](LICENSE).

---

## 👨‍💻 Authors

- **Abdul Qadir** – University of Balochistan  
  ORCID: https://orcid.org/0009-0004-0413-488X
- **Ihsan Ullah**

---

## 📖 Citation

If you use this toolkit in your research, please cite the following paper:

> Abdul Qadir (2024). *Pashto Text Preprocessing for Low-Resource Language: Pashto Language*. Journal of Open Source Software.

```bibtex
@article{qadir2024pashto,
  title={Pashto Text Preprocessing for Low-Resource Language: Pashto Language},
  author={Qadir, Abdul},
  journal={Journal of Open Source Software},
  year={2024},
  publisher={The Open Journals}
}
```

---

## 🙏 Acknowledgments

Developed as part of an MS research project in Pashto NLP. Supported by open-source software and community efforts to process low-resource languages.
