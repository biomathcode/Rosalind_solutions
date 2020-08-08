from __future__ import print_function
from collections import Counter
from itertools import chain

edges = []
with open("docs/rosalind_deg.txt", 'r') as f:
    next(f)
    for line in f:
        edges.append(line.strip().split())
f.close()

my_list = []
for x in chain.from_iterable(edges): #flatten the lists
    my_list.append(x)

##Counter accept a list and returns the count of each occurance of a list

d = Counter(my_list)

o = open("submission.txt", 'w')
#Sorted will sort the list based on number
for key in sorted(d, key = int):
    print(d[key], end=" ", file= o)
o.close()
