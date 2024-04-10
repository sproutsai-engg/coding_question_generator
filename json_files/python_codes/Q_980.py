##Question ID: 980

from itertools import permutations

def smallestSuperstring(words):
    def get_shared_length(a, b):
        for shared_length in range(min(len(a), len(b)), 0, -1):
            if a[-shared_length:] == b[:shared_length]:
                return shared_length
        return 0

    def merge(a, b, shared_length):
        return a + b[shared_length:]

    def get_total_length(merged_words):
        return sum(len(word) for word in merged_words)

    best = None
    for perm in permutations(words):
        merged_words = list(perm)
        for i in range(len(words) - 1):
            shared_length = get_shared_length(merged_words[i], merged_words[i + 1])
            merged_words[i + 1] = merge(merged_words[i], merged_words[i + 1], shared_length)
        if best is None or get_total_length(merged_words) < len(best):
            best = "".join(merged_words)

    return best

## Structure
from itertools import permutations
    # Your code here

    pass