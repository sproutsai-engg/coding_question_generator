##Question ID: 30

from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []

    word_count = Counter(words)
    word_length = len(words[0])
    total_words = len(words)
    total_length = word_length * total_words
    result = []

    for i in range(len(s) - total_length + 1):
        temp_word_count = Counter()
        for j in range(total_words):
            current_word = s[i + j * word_length:i + (j + 1) * word_length]
            if current_word not in word_count:
                break
            temp_word_count[current_word] += 1
            if temp_word_count[current_word] > word_count[current_word]:
                break
            if j + 1 == total_words:
                result.append(i)

    return result

## Structure
from collections import Counter
    # Your code here

    pass