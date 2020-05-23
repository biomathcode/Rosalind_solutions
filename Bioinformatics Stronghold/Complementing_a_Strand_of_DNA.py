"""FINDIND THE REVERSE COMPLEMENT"""

## AAAACCCGGT
## ACCGGGTTTT

s = input("Type the DNA sequence here")

complement = s.translate(str.maketrans({'A': 'T', 'T':'A', 'C': 'G', 'G' : 'C'}))

def reverse(string):
    string = string[::-1]
    return string
reverse_complement = reverse(complement)

print(reverse_complement)

file = open('reverse_complement.txt', 'w')

file.write(reverse_complement)


