"""
Given: A collection of n (n≤10) GenBank entry IDs.

Return: The shortest of the strings associated with the IDs in FASTA format.
"""
##Sample dataset 
#FJ817486 JX069768 JX469983

from Bio import Entrez
from Bio import SeqIO

##TODO:- organise the code

Entrez.email = "sharma.pratik2016@gmail.com"
handle = Entrez.efetch(db="nucleotide", id =["JX069768, JX472277, NM_001015511, JX460804, JQ290344, JQ712977, JX295575, NM_002124, FJ817486, JX569368"], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))

seq = list()
for i in range(len(records)):
    seq.append(len(records[i].seq))
print(seq)
maxIndex = seq.index(min(seq))
with open("submission.txt", 'w') as f:
    print(">" + records[maxIndex].description + '\n' + records[maxIndex].seq ,file=f)
