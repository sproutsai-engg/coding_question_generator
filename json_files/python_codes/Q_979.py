##Question ID: 979

def decode_permutation(s: str):
    n = len(s)
    perm = [0] * (n + 1)
    next_zero, next_one = 0, n

    for c in s:
        if c == '0':
            perm[next_zero] = next_one
            next_zero += 1
            next_one -= 1
        else:
            perm[next_one] = next_zero
            next_one -= 1
            next_zero += 1

    perm[next_zero] = next_one
    return perm


## Structure
def decode_permutation(s: str):
    # Your code here

    pass