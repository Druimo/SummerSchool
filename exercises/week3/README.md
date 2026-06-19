# Week 3 Exercise Starters

This folder contains small starter assets for the Week 3 foundation-model exercises.

## Reproducibility Requirements

**Dependencies:**
- Python 3.9+
- Python packages required for the Colab notebook: `torch`, `transformers`, `scikit-learn`, `umap-learn`, `matplotlib`, `seaborn`, `pandas`. 
- See `requirements.txt` to install them locally using pip:
  ```bash
  pip install -r requirements.txt
  ```

## Exercise A: Structure Prediction

**Input:** A short protein sequence (e.g., BRAF fragment).
**Output:** Predicted structures (PDB), pLDDT plots, PAE matrices, coverage plots.

Use this public notebook:
- [ColabFold AlphaFold2 notebook](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)

Keep inputs small (1-3 proteins or domains under roughly 200 amino acids).

## Exercise B: Protein Embeddings

**Input:** `protein_accessions.tsv`
**Output:** `proteins.fasta` and resulting plots (Cosine Similarities, PCA, UMAP)

### Steps to Rerun:

1. **Build the starter FASTA from UniProt:**
   This reads `protein_accessions.tsv` and writes `proteins.fasta`.
   ```bash
   python3 fetch_proteins.py
   ```

2. **Compute Embeddings & Clustering:**
   In Colab or a local Jupyter environment, use [`B_protein_embeddings_esm2.ipynb`](./B_protein_embeddings_esm2.ipynb).
   - If using Colab, you MUST upload these two files before running the cells:
     - `protein_accessions.tsv`
     - `proteins.fasta`
   - Run all cells sequentially. 
   - The notebook relies on the packages listed in `requirements.txt`.

## Exercise C: Optional Genomic Benchmarks

Use a fresh notebook or script. These links are useful starting points:
- [Genomic Benchmarks repository](https://github.com/ML-Bioinfo-CEITEC/genomic_benchmarks)
- [Nucleotide Transformer v2 50M multi-species model card](https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-50m-multi-species)

Write your final numbers and short interpretation in `results.md`.
