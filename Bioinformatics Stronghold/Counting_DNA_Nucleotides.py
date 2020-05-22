str = input(" Type the ACGT sequence here")

file = open('./rosalind_dna.txt', 'r')
string = file.read()
counts = {
    "A": 0,
    "C" : 0,
    "G" : 0,
    "T" : 0
}
for i in string:
    counts[i] += 1
print(counts.values())

def qt(s):
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")