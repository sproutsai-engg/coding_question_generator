##Question ID: 1764

def max_k_repeating(sequence, word):
    max_k = 0
    seq_length = len(sequence)
    word_length = len(word)
    for i in range(seq_length - word_length + 1):
        k = 0
        while sequence[i:i + word_length * (k + 1)] == word * (k + 1):
            k += 1
        max_k = max(max_k, k)
    return max_k

## Structure
def max_k_repeating(sequence, word):
    # Your code here

    pass