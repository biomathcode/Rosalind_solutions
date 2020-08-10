from Bio import ExPASy
from Bio import SwissProt
from Bio import SeqIO

with ExPASy.get_sprot_raw("Q5SLP9") as handle:
    seq_record = SeqIO.read(handle, "swiss")

print(dir(seq_record))
print(seq_record.annotations["keywords"])