"""
Calculate the GC content
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Difficulty level = ***

"""

Sample_data = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

def Percent(sequence):
    G_count = sequence.count ('G')
    C_count = sequence.count ('C')
    Total_count = len(sequence)
    GC_Sum = int(G_count) + int(C_count)
    Percent_GC = GC_Sum / Total_count
    Per_GC = (Percent_GC)*100
    return Per_GC
def readGenome(filename):
    with open(filename, 'r') as f:
        fasta_dictionary = {}
        sequence_name = ""
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                sequence_name = line[1:]
                if sequence_name not in fasta_dictionary:
                    fasta_dictionary[sequence_name] = []
                continue
            sequence = line
            fasta_dictionary[sequence_name] = sequence

    dictionary = dict()
    for sequence_name in fasta_dictionary:
        dictionary[sequence_name] = float
    for sequence_name, sequence in fasta_dictionary.items():
        inverse = [(sequence, sequence_name) for sequence_name, sequence in dictionary.items()]
        highest_GC = max(inverse)[1] 

    for sequence_name, sequence in fasta_dictionary.items():
        if sequence == highest_GC:
             return print ((sequence_name) + ' ' + (highest_GC)) 


if __name__ == "__main__":
    readGenome = readGenome('sample.fa')
    print(readGenome)
