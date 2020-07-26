#findind the all the index of the sub-string from string
#GATATATGCATATACTT
#ATAT
import re
def regrex_occurence(test_string, sub_string):
    res = [i.start() for i in re.finditer(test_string, sub_string)]
    return res

reg_occ = regrex_occurence("This is a string whis is alis", "is")
print(reg_occ)
#Sample output
#2 4 10
def AllOccurence(test_string, sub_string):
    res = [ i+1 for i in range(len(test_string)) if test_string.startswith(sub_string, i)]
    return res

test_string = input('this is the input string :-')
sub_string = input("this is the pattern to find:- ")
occurence = AllOccurence(test_string, sub_string)
print(occurence)

#other solutions that i liked
s1 ,s2 = open('rosalind_subs.txt').read().split('\r\n')

for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print(i+1,)