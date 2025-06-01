---
title: 'Pashto Text Preprocessing Toolkit for Low-Resource Language'
authors:
- name: Abdul Qadir
  affiliation: 1
  orcid: 0009-0004-0413-488X
- name: Ihsan Ullah
  affiliation: 1
affiliations:
- name: Department of Computer Science, University of Balochistan, Pakistan
  index: 1
date: 2025-05-26
---

# Summary

This toolkit provides an end-to-end preprocessing pipeline for Pashto, a low-resource language spoken primarily in Pakistan and Afghanistan. It includes modules for normalization, tokenization, stopword removal, stemming, lemmatization, and TF-IDF computation. The toolkit is tailored to the linguistic features of Pashto, offering rule-based POS tagging and configurable resource mappings.

The toolkit is designed to be modular and easy to integrate into NLP pipelines for downstream tasks like classification, summarization, and information retrieval.

# Statement of need

Pashto suffers from a lack of linguistic tools and standardized datasets. This preprocessing toolkit fills that gap by offering an open-source, tested, and extensible Python-based solution. It is valuable for linguists, researchers, and developers working on Pashto or similar low-resource languages [@ref1_n.d.], [@ref2_2015], [@ref3_2023], [@ref4_2023], [@ref5_2009], et al.

# Installation

```bash
pip install .
```

# Usage

```python
from pashto_nlp import normalize_text, tokenize
text = "زه مکتب ته ځم"
print(tokenize(normalize_text(text)))
```

# Repository

The software is available at: https://github.com/AryanQadir/Pashto_Text_Preprocessing

# Acknowledgements

This work was carried out as part of an MS research project under the supervision of the University of Balochistan.

# References
