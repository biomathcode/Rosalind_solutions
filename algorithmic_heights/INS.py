'''

Given: A positive integer n≤103 and an array A[1..n] of integers.

Return: The number of swaps performed by insertion sort algorithm on A[1..n].



'''
from itertools import chain
def parser_arr(file_name):
    with open(file_name) as f:
        next(f)
        arr = [item.split() for item in f.readlines()]
    arr1 = []
    for x in chain.from_iterable(arr):
        arr1.append(int(x))
    return arr1
def insertion_sort(arr, count = 0):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            count += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return count, arr

if __name__ == "__main__":
    file_name = 'docs/' + input('file name here:-')
    arr = parser_arr(file_name)
    print(insertion_sort(arr))
    arr, count = insertion_sort(arr)
    print(arr)
