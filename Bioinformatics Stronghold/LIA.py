##INDEPENDENT ALLELES

""" Mendel's seconds Law

Law of independent assortement """

## independent probability of two random varibles X and Y = Pr(x) * Pr(y)
## X+ Y is odd
## X => even, Y => odd
## Y => even, X => odd
from math import factorial as ft

def probabilityOfAaBb(k, n):
     ## no. of organisms
    # what we have to do 
    # find out the probability of atleast N org will belong to the k-th generation
    # simple binomial probability
    P = 2**k
    p = 0.25
    q = 1- p
    proba = 0
    for i in range(n, P+1):
        probability = (ft(P)/(ft(i) * ft(P -i))) * (p**i) * (q**(P-i)) 
        print(probability)
        proba += probability

    return print("/probabilit:", round(proba, 3))

probabilityOfAaBb(5,9)