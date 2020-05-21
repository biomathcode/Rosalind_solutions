
while True:
    try: 
        a, b, c = [int(x) for x in input("start, end and odd(1) even(0)").split()]
        print(a, b, c, "Are the values that you have decided")
        break
    except ValueError:
        print('Please give four indices')

"""function can find the sum of odd and even numbers from range (a, b)"""
def SumOfNumbers(a, b, c):
    count = 0
    for i in range(a,b):
        if i % 2 == c:
            count += i
    number = "odd" if c == 1 else "even"
    return print("the sum of", number, "numbers from", a , "to ", b, "is" , count )

SumOfNumbers(a, b, c)

"""Input = 4642 to 8652
output = 13327235
"""

