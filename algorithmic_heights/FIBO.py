#first creating a dynamic function for calculating fibonacci function
def dynFibonacci(n):
    store = {}
    store[0], store[1] = 0,1
    #print(store)
    for i in range(2, n+1):
        store[i] = store[i -1] + store[i-2]
    #print(store)
    return store[n]

if __name__ == "__main__":
    number = int(input('the nth fibonacci number is'))
    print(dynFibonacci(number))