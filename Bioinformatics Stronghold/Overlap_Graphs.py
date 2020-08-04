### Creating Overlapping Graphs
from Bio import SeqIO
import itertools

Seq_dic = dict()
def dictionar_seq(file_name):  
    with open('docs/' + file_name, 'r') as f:
        for dna_record in SeqIO.parse(f, 'fasta'):
            sequence = dna_record.seq
            name = dna_record.name
            Seq_dic[name] = sequence
        return Seq_dic

def is_k_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]

def k_edges(data,k):
    edges = []
    for u,v in itertools.combinations(data, 2):
        u_dna , v_dna = data[u], data[v]
        if is_k_overlap(u_dna, v_dna, k):
            edges.append((u,v))
        if is_k_overlap(v_dna, u_dna, k):
            edges.append((v,u))

    return edges