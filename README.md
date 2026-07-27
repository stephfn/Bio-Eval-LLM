# Bio-Eval-LLM: Automated Benchmarking Framework for Drug Discovery AI Prompts

![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Domain: Computational Biology & AI](https://img.shields.io/badge/Domain-Translational%20Science%20%26%20RLHF-green)

An automated evaluation and error-detection framework designed to benchmark AI-generated scientific reasoning in **drug discovery, molecular assay design, and genomic workflows**. 

This repository simulates Reinforcement Learning from Human Feedback (RLHF) and expert domain evaluation pipelines. It uses rule-based domain checks, semantic similarity scoring, and custom evaluation metrics to identify scientific hallucinations, incorrect assay controls, and data scaling anomalies in LLM-generated biological outputs.

---

## Key Features

* **Domain-Specific Rule Engine:** Validates experimental protocol logic, positive/negative assay controls, and stoichiometry rules across multi-step biological pipelines.
* **Semantic & Text Similarity Scoring:** Measures response fidelity against ground-truth scientific benchmarks using `scikit-learn` cosine similarity and NLP metrics.
* **Hallucination & Error Classification:** Automatically categorizes AI failures into biological reasoning errors, missing experimental parameters, or data normalization flaws.
* **Visual Evaluation Analytics:** Generates automated diagnostic reports comparing model accuracy across distinct drug discovery domains.

---

## Repository Structure

```text
Bio-Eval-LLM/
├── data/
│   └── eval_dataset.json          # Synthetic benchmark dataset (Prompts, Ground Truth, AI Responses)
├── src/
│   └── evaluator.py               # Core evaluation engine & metric calculators
├── .gitignore                     # Git tracking exclusions
├── requirements.txt               # Dependencies (pandas, scikit-learn, etc.)
└── README.md                      # Project documentation
```

## Technical Stack & Libraries

* **Core Language:** Python 3.10+
* **Data Processing & Analytics:** `pandas`, `NumPy`
* **Machine Learning & NLP Metrics:** `scikit-learn` (TfidfVectorizer, Cosine Similarity)
* **Development Environment:** GitHub / Jupyter Notebook

---

## Quickstart & Usage

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/stephfn/Bio-Eval-LLM.git](https://github.com/stephfn/Bio-Eval-LLM.git)
   cd Bio-Eval-LLM

---

## Author

**Stephanie Nord**  
*M.S. in Data Science | B.S. in Biology*  
*Specializing in Computational Biology, High-Throughput Molecular Diagnostics, and Machine Learning*  
[LinkedIn](https://www.linkedin.com/in/stephanienord) | [GitHub](https://github.com/stephfn)
