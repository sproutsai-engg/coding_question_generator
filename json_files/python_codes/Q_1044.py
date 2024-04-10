##Question ID: 1044

from collections import Counter

def commonChars(words):
    merged = Counter()
    for word in words:
        word_count = Counter(word)
        if not merged:
            merged = word_count
        else:
            for char in merged:
                merged[char] = min(merged[char], word_count[char])

    result = []
    for char, count in merged.items():
        result.extend([char] * count)
    return result

## Structure
from collections import Counter
    # Your code here

    pass