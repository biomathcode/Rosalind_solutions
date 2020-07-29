#finding the most common ancestor

# DNA string 

# Profile
'''
 >Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
'''

'''
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''
from Bio import SeqIO
import numpy as np
np.set_printoptions(threshold=np.inf)

dna_name, dna_sequence = [], []

with open('docs/rosalind_cons.txt', 'r') as f:
    for dna_record in SeqIO.parse(f, 'fasta'):
        dna_name.append(str(dna_record.name))
        print(dna_record.name)
        dna_sequence.append(str(dna_record.seq))

dnaSeq_len = len(dna_sequence) 
dna_bases = len(dna_sequence[0])
print(dna_bases, dnaSeq_len)
bases = ['A', 'C' ,'G', 'T']
consense_seq = ''
profile_matrix = np.zeros(shape=(4, dna_bases), dtype=int)

for c in range(dna_bases):
    #gets the first base from all the sequnces
    position_bases = [s[c] for s in dna_sequence]
    # Counts the most common Base on the key position
    most_common_base = max(position_bases, key=position_bases.count)
    
    consense_seq += most_common_base
    for r in range(len(bases)):
        profile_matrix[r][c] = position_bases.count(bases[r])

print(consense_seq)
matrix = ""
for i in range(len(bases)):
    matrix += "{}: {} \n".format(bases[i], " ".join([str(j) for j in profile_matrix[i]]))

print(matrix)
submission_file = open('submission.txt', 'w')
submission_file.write(consense_seq)
submission_file.write('\n')
submission_file.write(matrix)
submission_file.close()








