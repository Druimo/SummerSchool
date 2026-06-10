import argparse
import os
import sys

def parse_fasta(filepath_or_seq):
    """Parses a FASTA file or treats the input as a raw sequence."""
    if os.path.isfile(filepath_or_seq):
        sequences = {}
        current_header = None
        current_seq = []
        with open(filepath_or_seq, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith(">"):
                    if current_header:
                        sequences[current_header] = "".join(current_seq)
                    current_header = line[1:]
                    current_seq = []
                else:
                    current_seq.append(line)
            if current_header:
                sequences[current_header] = "".join(current_seq)
        return sequences
    else:
        # Treat as raw sequence input
        seq = filepath_or_seq.strip().replace("\n", "").replace("\r", "")
        # Remove FASTA header if present in raw string
        if seq.startswith(">"):
            parts = seq.split("\n", 1)
            if len(parts) > 1:
                return {parts[0][1:]: parts[1]}
            else:
                return {"sequence": ""}
        return {"input_sequence": seq}

def analyze_sequence(sequence):
    """Calculates standard bioinformatic statistics for a genomic sequence."""
    seq_upper = sequence.upper()
    length = len(seq_upper)
    
    if length == 0:
        return {
            "length": 0,
            "gc_content": 0.0,
            "base_counts": {},
            "base_freqs": {},
            "cpg_obs": 0,
            "cpg_ratio": 0.0
        }
    
    # Base counts
    bases = ['A', 'C', 'G', 'T', 'N']
    counts = {b: seq_upper.count(b) for b in bases}
    other_count = sum(1 for char in seq_upper if char not in bases)
    if other_count > 0:
        counts['Other'] = other_count
        
    freqs = {b: (count / length) * 100 for b, count in counts.items()}
    
    # GC content
    gc_count = counts.get('G', 0) + counts.get('C', 0)
    gc_content = (gc_count / length) * 100 if length > 0 else 0.0
    
    # CpG ratio (Observed / Expected)
    # Observed CpG count
    cpg_obs = seq_upper.count("CG")
    c_count = counts.get('C', 0)
    g_count = counts.get('G', 0)
    
    if c_count > 0 and g_count > 0:
        # Expected CpG = (C * G) / L
        # Obs / Exp = Observed / Expected = Observed / ((C * G) / L) = (Observed * L) / (C * G)
        cpg_ratio = (cpg_obs * length) / (c_count * g_count)
    else:
        cpg_ratio = 0.0
        
    return {
        "length": length,
        "gc_content": gc_content,
        "base_counts": counts,
        "base_freqs": freqs,
        "cpg_obs": cpg_obs,
        "cpg_ratio": cpg_ratio
    }

def print_report(name, stats):
    """Prints sequence statistics in a concise, standard format."""
    print(f"=== Analysis for Sequence: {name} ===")
    print(f"Length: {stats['length']} bp")
    print(f"GC Content: {stats['gc_content']:.2f}%")
    print("Base Composition:")
    for b in sorted(stats['base_counts'].keys()):
        count = stats['base_counts'][b]
        freq = stats['base_freqs'][b]
        print(f"  {b}: {count:8d} ({freq:6.2f}%)")
    print(f"CpG Dinucleotides (CG): {stats['cpg_obs']} (Obs/Exp Ratio: {stats['cpg_ratio']:.3f})")
    print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description="Genomic sequence statistical analysis tool.")
    parser.add_argument("input", help="FASTA file path or raw sequence string")
    args = parser.parse_args()
    
    try:
        sequences = parse_fasta(args.input)
        if not sequences:
            print("No sequences found.", file=sys.stderr)
            sys.exit(1)
            
        for name, seq in sequences.items():
            stats = analyze_sequence(seq)
            print_report(name, stats)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
