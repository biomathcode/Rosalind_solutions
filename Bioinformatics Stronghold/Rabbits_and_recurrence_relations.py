"""
GIVEN :- Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

"""

def fibonacci_with_k_children(n, k):

    if n == 0 or n == 1:
        value = n
    else:
        value = fibonacci_with_k_children(n -1, k) + (k * fibonacci_with_k_children(n-2, k))
    return(value)




if __name__ == "__main__":
    a = int(input('Number of months for reproduction'))
    b = int(input(" Number of children per 2 months"))

    result = fibonacci_with_k_children(a,b)
    print(result)

##TODO : - This is recursion based make it a dynamic one
## Here is the code for a fibonacci sequence in DP
def fib(n):
    fibtable = {}
    fibtable[0] = 0
    fibtable[1] = 1

    for i in range(2, n+1):
        fibtable[i] = fibtable[i-1] + fibtable[i-2]

    return(fibtable[n])