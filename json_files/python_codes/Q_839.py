##Question ID: 839

def minimal_length_encoding(words):
    word_set = set(words)

    for word in words:
        for i in range(1, len(word)):
            word_set.discard(word[i:])

    return sum(len(word) + 1 for word in word_set)

## Structure
def minimal_length_encoding(words):
    # Your code here

    pass