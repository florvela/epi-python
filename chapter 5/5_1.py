# Dutch national flag problem

def dutch_flag(arr, i):
    ## less , equal, greater
    pivot = arr[i]

    # indexes
    less = 0
    equal = 0
    greater = len(arr)

    while equal < greater:
        if arr[equal] < pivot:
            arr[less], arr[equal] = arr[equal], arr[less]
            less += 1
            equal += 1
        elif arr[equal] > pivot:
            greater -= 1
            arr[greater], arr[equal] = arr[equal], arr[greater]
        else:
            equal += 1

    print(arr)

"""
pivot = 2
[1,2,3,2,1,3]
equal = 2
less = 2
greater = 4

"""

dutch_flag([1,3,2,2,1,2], 2)