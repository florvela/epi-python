# multiply two arbitrary-precision integers

# take 2 arrays representing ints and return their product

def multiply(num1, num2):
    res_len = len(num1) + len(num2)
    result = [0] * res_len

    sign = -1 if num1[0] * num2[0] < 0 else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            if result[i + j + 1] > 10:
                result[i + j] += result[i + j + 1] // 10
                result[i + j + 1] = result[i + j + 1] % 10

    for start in range(len(result)):
        if result[start] != 0:
            result[start] = result[start] * sign
            return result[start:]

"""
[1,0,2] x [3,2]

                4
            6
            0
        0
        2
    3
    3264

[5,6] x [1,5]
                30
            6
            25
        5
        [5,31,30]
        [5,31+3,0]
        [5,34,0]
        [5+3,4,0]
        [8,4,0]


"""

print(multiply([1,0,2], [3,2]))
print(multiply([5,6], [1,5]))
print(multiply([-1,0,2], [3,2]))
print(multiply([-5,6], [-1,5]))
