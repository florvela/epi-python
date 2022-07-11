# count the number of bits set to 1 in a non-negative integer

def count_bits(input_int: int) -> int:
    num_bits = 0
    while input_int:
        num_bits += input_int & 1
        input_int = input_int >> 1
    return num_bits