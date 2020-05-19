a = int(input('this is the a length of triangle : '))
b = int(input('this is the b length of triangle : '))

def square_hypotenuse(a = 3, b = 5):
    a_square = a * a
    b_square = b * b
    hypotenuse = a_square + b_square 
    return print("The hypotenuse is ", hypotenuse)

square_hypotenuse(a ,b)

"""
this is the a length of triangle : 966
this is the b length of triangle : 971
The hypotenuse is  1875997
"""