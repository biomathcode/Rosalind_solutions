## Binary search with 

'''
Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from −105 to 105 and a list of m integers −105≤k1,k2,…,km≤105.

Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.

'''
def parser_for_binary_search(file_name):
    print('This function is working')
    with open(file_name) as f:
        _, _, xlist, ylist = [line.strip().split() for line in f.readlines()]
        xlist = [int(num) for num in xlist]
        ylist = [int(num) for num in ylist]
        return xlist, ylist

def binary_search(yvalue, xarray):
    print('binary_search')
    x_beg = 0
    x_end = len(xarray) -1
    while x_beg <= x_end:
        x_mid = (x_beg + x_end) // 2
        if xarray[x_mid] == yvalue: 
            return  x_mid + 1
        elif yvalue > xarray[x_mid]  :
            x_beg = x_mid + 1
        else: 
            x_end = x_mid -1  
            
    return -1

def index_finder(xarray, yarray):
    indices = []
    for y in yarray:
        index = binary_search(y, xarray)
        print(
            'binary search ends here'
        )
        indices.append(index)
    return indices

if __name__ == "__main__":
    file_name = 'docs/' + input('file name here :- ')
    xarray, yarray = parser_for_binary_search(file_name)
    print(xarray, yarray)
    indices = index_finder(xarray,yarray)
    print(indices)
    indices_table = ''
    for i in indices:
        indices_table += '{} '.format(i)
    print(indices_table)
    submission_file = open('submission.txt', 'w')
    submission_file.write(indices_table)
    submission_file.close()

        
# def Binary_search(Array, item):
#     low = 0
#     high = len(Array)-1
#     while low <= high:
#         index = (low + high) // 2
#         if item == Array[index]:
#             return index + 1
#         elif item > Array[index]:
#             low = index + 1
#         else:
#             high = index - 1
#     return -1

# with open('docs/sample.txt','r') as file:
#     content = file.read().splitlines()

# array = [int(i) for i in content[2].split()]
# items = [int(i) for i in content[3].split()]
# line = ''

# for i in range(len(items)):
#     line += str(Binary_search(array, items[i])) + ' '

# print(line)
