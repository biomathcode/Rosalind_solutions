import re

DNA_sequence = input('DNA sequence')


RNA_sequence = re.sub(r'T', "U",DNA_sequence)

print(RNA_sequence)

file = open("copy.txt", 'w')

file.write(RNA_sequence)

file.close()