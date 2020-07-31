'''
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample dataset:-
6 3

Sample output:

4

'''

#first creating a dynamic function for calculating fibonacci function
def dynFibonacci(n):
    store = {}
    store[0], store[1] = 0,1
    print(store)
    for i in range(2, n+1):
        store[i] = store[i -1] + store[i-2]
    print(store)
    return store[n]

def mortalFibonacci(n,k=1):
    rabbits = [1] + [0]*(k-1)
    for i in range(n-1):
        rabbits = [sum(rabbits[1:])] + rabbits[:-1]    
    return sum(rabbits)

print(mortalFibonacci(100,17))

    

