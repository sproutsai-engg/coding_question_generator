##Question ID: 318

def maxProduct(words):
    n = len(words)
    mask = [0] * n
    for i, word in enumerate(words):
        for c in word:
            mask[i] |= (1 << (ord(c) - ord('a')))
    
    max_product = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (mask[i] & mask[j]) == 0:
                max_product = max(max_product, len(words[i]) * len(words[j]))
    
    return max_product


## Structure
def maxProduct(words):
    # Your code here

    pass