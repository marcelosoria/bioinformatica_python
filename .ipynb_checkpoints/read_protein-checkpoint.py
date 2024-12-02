from Bio import SeqIO

def read_protein_sequences(filename):
    for record in SeqIO.parse(filename, "genbank"):
        print(f"Protein ID: {record.id}, Description: {record.description}")
        print(f"Common name: {record.annotations['source']}")
        print(f"Sequence: {record.seq}")
        for feature in record.features:
            print(feature.type)
            if feature.type == "CDS":
                locus_tag = feature.qualifiers.get('locus_tag')
                if locus_tag:
                    print(f"Locus tag: {locus_tag[0]}")

read_protein_sequences("sequence.gp")


