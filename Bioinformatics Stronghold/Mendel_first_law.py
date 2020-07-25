from scipy.special import comb

def calculateProbability(k, m, n):
    #K is homozygous dominant
    #m is heterzygous 
    #n is homozygous recessive
    #Calcuate the probability of homozygos allege
    total = k + m + n
    # Calculating the total number of combos that could be made(valid or not):
    total_combos = comb(total, 2)
    #Dominant Alleles
    valid_combos = comb(k,2) + k*m + k*n + .5*m*n + 0.75*comb(m,2)
    probability = valid_combos/total_combos

    return probability
k = int(input('number of homozygous dominant :-'))
m = int(input('number of heterzygous :- '))
n = int(input('number of homozygous recessive :- '))
print(calculateProbability(k,m,n))

    
    
    