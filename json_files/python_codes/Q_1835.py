##Question ID: 1835

def decode(encoded):
    n = len(encoded) + 1
    total_xor = 0
    for i in range(1, n + 1):
        total_xor ^= i
    encoded_xor = 0
    for i in range(1, n - 1, 2):
        encoded_xor ^= encoded[i]
    perm = [total_xor ^ encoded_xor]
    for i in range(1, n):
        perm.append(perm[-1] ^ encoded[i - 1])
    return perm

## Structure
def decode(encoded):
    # Your code here

    pass