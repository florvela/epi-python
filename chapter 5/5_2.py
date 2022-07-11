# increment an arbitrary precision integer

"""
[0]         => [1]
[9]         => [1,0]
[1,0]       => [1,1]
[9,9]       => [1,0,0]
[1,2,9]     => [1,3,0]
"""

def add_one(num):

    for i in reversed(range(len(num))):
        num[i] += 1
        if num[i] < 10:
            break

        num[i] = num[i] % 10

    if num[0] == 0:
        num[0] = 1
        num.append(0)
    return num

print(add_one([9,9]))
print(add_one([1,2,3]))
print(add_one([1,2,9]))
print(add_one([9]))