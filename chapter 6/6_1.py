

def string_to_int(input_string):
    digits = "0123456789"
    start = 0
    sign = 1
    if input_string[start] == "-":
        sign = -1
        start += 1
    elif input_string[start] == "+":
        start += 1

    result = 0
    multiplier = 1
    for i in reversed(range(start, len(input_string))):
        result += digits.index(input_string[i]) * multiplier
        multiplier = multiplier * 10

    result = sign * result
    return result

def int_to_string(input_int):
    digits = "0123456789"
    result = ''
    if input_int < 0:
        sign = '-'
        input_int = input_int * -1
    else:
        sign = ''
    while True:
        digit = input_int % 10
        result += digits[digit]
        input_int = input_int // 10
        if input_int == 0:
            break

    return sign + result[::-1]

print(string_to_int("123"))
print(string_to_int("-123"))
print(string_to_int("+123"))
print(string_to_int("1"))
print(string_to_int("-1"))
print(int_to_string(123))
print(int_to_string(-123))
print(int_to_string(0))
print(int_to_string(1))
print(int_to_string(10000))
print(int_to_string(10))
