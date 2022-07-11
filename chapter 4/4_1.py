# computing the parity of a word
# 1 if the number of 1s is odd, else 0

########### O(N)
def parity(x: int) -> int:
    result = 0
    while x:
        result = result ^ x & 1
        x >>= 1
    return result

# TODO: check el libro