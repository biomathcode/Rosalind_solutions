## two sequence and 
#seq 1
#seq 2
#output the number of point mutations 
def humming_distance(seq1, seq2):
    cnt = 0
    for i in range(len(seq1)):
        if seq1[i] is not seq2[i]:
            cnt += 1
            
    return print(cnt)
f = open("docs/rosalind_hamm.txt", 'r')
seqences = f.readlines()
print(seqences)
seq1 = seqences[0]
seq2 = seqences[1]
print(seq1)
print(seq2)
humming_distance(seq1, seq2)