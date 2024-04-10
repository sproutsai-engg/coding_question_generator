##Question ID: 952

from collections import Counter

def word_subsets(words1, words2):
    max_chars = Counter()
    for word in words2:
        chars = Counter(word)
        for c, count in chars.items():
            max_chars[c] = max(max_chars[c], count)
    
    result = []
    for word in words1:
        word_chars = Counter(word)
        universal = all(word_chars[c] >= max_chars[c] for c in max_chars)
        if universal:
            result.append(word)
    
    return result


## Structure
from collections import Counter
    # Your code here

    pass