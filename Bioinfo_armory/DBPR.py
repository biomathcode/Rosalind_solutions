from Bio import ExPASy
from Bio import SwissProt
from Bio import SeqIO

def getgo(id):
    handle = ExPASy.get_sprot_raw(id)
    record = SwissProt.read(handle)
    go = [r[2].split(":")[1] for r in record.cross_references if r[0] == "GO" and  r[2].startswith("P")]
    print("\n".join(go))

getgo("Q5SLP9")