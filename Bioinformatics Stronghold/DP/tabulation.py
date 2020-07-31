def f(n):
    array = [0]*(n+1)
    
    #base case
    array[1] = 1
    for i in range(2, n+1):
        array[i] = array[i-1] + array[i-2]
    return array[n]

def main(): 
    n = 9
    print("Fibonacci number is ", f(n)) 
  
if __name__=="__main__": 
    main() 