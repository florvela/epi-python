# reorder array so that even appear first

def even_odd(arr):
    next_even = 0
    next_odd = len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1

    print(arr)

"""
[1, 2, 3, 4] => [2, 4, 1, 3]
[2] => [2]
"""

even_odd([1])