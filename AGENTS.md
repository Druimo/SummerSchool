# Agent Instructions for this Repository

When working in this repository, follow these rules:

1. **Python Environment**: Assume Python 3.9+. When installing packages, use `pip` with `requirements.txt` instead of `uv`.
2. **Data Files**: Expect raw genomic or protein data (e.g., FASTA, TSV, GFF3) in the `exercises/` subdirectories. Do not modify raw data files.
3. **Genomic Coordinates**: Remember that GFF3 files use 1-based, inclusive coordinates, whereas Python slicing is 0-based and exclusive. Always adjust coordinates (e.g., `-1`) when slicing strings.
4. **Validation Checks**: When extracting Coding Sequences (CDS) or proteins, automatically validate that they start with an 'M' (Methionine), end with a '*' (stop codon), and that the nucleotide length is divisible by 3.
5. **Output Restrictions**: Never overwrite `lessons.md` or `results.md` entirely; only append or replace specific sections.
6. **Execution**: Most deep learning models should be run in Colab due to compute constraints. Provide explicit instructions for Colab when generating model scripts.
