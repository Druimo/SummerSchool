from Bio import SeqIO
from Bio.Seq import Seq

def parse_gff(gff_path):
    cds_features = []
    with open(gff_path, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) < 9:
                continue
            if parts[2] == 'CDS':
                start = int(parts[3])
                end = int(parts[4])
                # Parse attributes
                attrs = {}
                for attr in parts[8].split(';'):
                    if '=' in attr:
                        key, val = attr.split('=', 1)
                        attrs[key] = val
                gene_name = attrs.get('Name', attrs.get('ID', 'unknown'))
                cds_features.append((gene_name, start, end))
    return cds_features

def main():
    # Load genome
    genome_record = next(SeqIO.parse('genome.fa', 'fasta'))
    genome_seq = str(genome_record.seq)
    
    # Load CDS features
    cds_features = parse_gff('annotations.gff3')
    
    # Process each CDS
    for gene_name, start, end in cds_features:
        # Extract sequence (GFF is 1-based inclusive, Python slice is 0-based exclusive)
        cds_seq = genome_seq[start - 1:end]
        
        # Translate to protein using standard genetic code
        protein_seq = str(Seq(cds_seq).translate())
        
        print(f"{gene_name}\t{cds_seq}\t{protein_seq}")

if __name__ == '__main__':
    main()
