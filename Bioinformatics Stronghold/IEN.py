## Calculating Expected offspring
"""
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""

def file_parser(file_name):
    with open("docs/" + file_name) as f:
        f = f.readline()
        ##number of offspring list
        offList = f.split(' ')
        offList = [int(x) for x in offList]
        print(offList)
    return offList
def expected_offspring(a):
    sum = (a[0] * 1 + a[1] * 1 + a[2] * 1 + a[3] *0.75 + a[4] *0.5 + a[5] * 0) * 2
    return sum
if __name__ == "__main__":
    file_name = input('Please type the filename here')
    offspring_list = file_parser(file_name)
    print(expected_offspring(offspring_list))
    


