# Week 3 Results

Use this file for the short Week 3 write-up. Keep it factual: what ran, what failed, what you checked, and what you would trust.

## Exercise A: Structure Prediction

- Tool or notebook: ColabFold (AlphaFold2)
- Sequence or target: Human BRAF (residues 401–480), sequence: `TPPASLPGSLTNVKALQKSPGPQRERKSSSSSEDRNRMKTLGRRDSSDDWEIPDGQITVGQRIGSGSFGTVYKGKWHGDV`
- Mean pLDDT: ~63
- Low-confidence regions: 1–45 .
- PAE observation, if relevant: The PAE plot shows a distinct well-defined block of low error (<10) for residues 45–80, representing the start of the kinase domain (stable folded structure). Conversely, the N-terminal region (1–45) shows extremely high PAE relative to both the kinase domain and itself. This confirms that while the kinase domain is rigid and well-folded, the N-terminal tail has no fixed spatial orientation relative to it and is highly flexible.
- Would you trust this prediction for a biological claim? Why or why not?: I would trust the structure of the C-terminal domain (residues 46–80) as it corresponds to a highly conserved part of the kinase domain

## Exercise B: Protein Embeddings

- Model: pre-trained ESM-2
- Number of sequences: 45
- Pooling choice: Mean-pooling
- Plot files: See: `exercises\week3\Exercise_B_results`
- Did known families cluster? Yes
- One validation check you performed: 
    - calculated the cosine similarity between the embeddings of the sequences in the dataset and compared it to the cosine similarity between the embeddings of the same sequences and themselves, 
        - Average cosine similarity within the same family: 0.9417
        - Average cosine similarity between different families: 0.7972  
        - Difference (Intra - Inter): 0.1444
    - used PCA on the embeddings to visualize them in a better space. 
    - used a NearestNeighbors analysis too see if the embeddings could be used to predict the family of the sequences 
        - Nearest Neighbor Accuracy (same family): 97.78% (44/45)

## Exercise C: Optional Genomic Benchmarks

- Dataset:
- Model:
- Embedding or fine-tuning setup:
- Accuracy:
- F1:
- Confusion matrix:
- Published CNN baseline you compared against:
- Interpretation:

## Surprises

List at least one model output that was hard to interpret and one validation habit you will reuse.
