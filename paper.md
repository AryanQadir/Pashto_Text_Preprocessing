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
bibliography: paper.bib
---

# Summary

This toolkit provides an end-to-end preprocessing pipeline Technique for Low-Resource Language: Pashto language (PTPTL), spoken primarily in Pakistan and Afghanistan. The PTPTL module performs essential steps including tokenization, normalization, stop-word removal, stemming, Prefix/suffix terms for normalization POS tagging and TF-IDF computation and is tailored to the linguistic features of Pashto, offering configurable resource mapping and rule-based POS tagging. A corpus of Pashto documents was used for evaluation. Through TF-IDF analysis, a high-frequency Pashto stop-word list was developed to enhance downstream processing. POS tagging was implemented using a rule-based method, improving the quality of syntactic analysis. Compared to the baseline approach, the Proposed PTPTL model achieved higher performance metrics across all measures, highlighting its effectiveness in processing Pashto text and offering a strong foundation for future research in low-resource language NLP.

The toolkit is designed to be modular and easy to integrate into NLP pipelines for downstream tasks like classification, summarization, and information retrieval.

# Statement of Need

Pashto suffers from a lack of linguistic tools and standardized datasets. This preprocessing toolkit fills that gap by offering an open-source, tested, and extensible Python-based solution. It is valuable for linguists, researchers, and developers working on Pashto or similar low-resource languages [@ref1_2022], [@ref2_2015], [@ref3_2023], [@ref6_2024], [@ref8_2010], [@ref9_2018], [@ref10_2013], [@ref11_2020], [@ref12_2017], [@ref13_2004], [@ref14_1995], [@ref15_2001].

# Installation

```bash
pip install pashto_text_preprocessing


# Usage

```md
from pashto_nlp import normalize_text, tokenize
...

from pashto_nlp import normalize_text, tokenize

text = "example_pashto_sentence"  # Example Pashto sentence
print(tokenize(normalize_text(text)))


# Repository

The full source code and documentation are available at:
https://github.com/AryanQadir/Pashto_Text_Preprocessing


# Acknowledgements

This work was carried out as part of an MS research project at the Department of Computer Science, University of Balochistan. We thank our supervisor and academic mentors for their continued support.


# References
---
