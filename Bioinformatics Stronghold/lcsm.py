"""
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

output:
CA
//Keeping in mind that the longest substring is not always unique

"""
from  Bio import SeqIO

arr_sequence = []
def multiple_seq(file_name):
    dna_name, dna_sequences = [], []
    with open(file_name) as f:
        for dna_record in SeqIO.parse(f, 'fasta'):
            dna_name.append(str(dna_record.name))
            dna_sequences.append(str(dna_record.seq))
    return dna_sequences

## Longest_common_substring in python 

def Longest_common_substring(s1, s2):
    m = [[0]* ( 1 + len(s2)) for i in range(1+len(s1))]

    longest, x_longest = 0,0
    for x in range(1, 1+ len(s1)):
        for y in range(1, 1+ len(s2)):
            if s1[x-1] == s2[y-1]:
                m[x][y] = m[x-1][y-1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] =0
    return s1[x_longest - longest: x_longest]

def LCS(dna_sequences):
    dna_sequences = sorted(dna_sequences, key=len)
    short_seq = dna_sequences[0]
    comp_seq = dna_sequences[1:]
    motif = ''

    for  i in range(len(short_seq)):
        for j in range(i, len(short_seq)):
            m = short_seq[i:j+1]
            found = False
            for sequ in comp_seq:
                if m in sequ:
                    found = True
                else:
                    found = False
                    break
            
            if found and len(m) > len(motif):
                motif = m
    return motif



if __name__ == "__main__":
    file_name = "docs/" + input('write the file_name:')
    seq_list = multiple_seq(file_name)
    lcs = LCS(seq_list)
    print(lcs)

