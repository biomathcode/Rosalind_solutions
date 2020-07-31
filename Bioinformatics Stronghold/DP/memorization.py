## memorization of top-down approach 

def fib(n, lookup):
    #initialising with the base case:
    if n == 0 or n == 1 :
        lookup[n] = n
    ## if the value is not calculated previouls then calculate it
    elif lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
    #return the value of corresponding to that value of n
    return lookup[n]

def main():
    n = 34

    lookup = [None]*(101)
    print(
        "The fibonacci number is ", fib(n, lookup)
    )
if __name__ == "__main__":
    main()