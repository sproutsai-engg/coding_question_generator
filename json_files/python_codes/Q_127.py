##Question ID: 127

from collections import deque

def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    q = deque([beginWord])
    steps = 1

    while q:
        size = len(q)
        current_level = set()
        
        for _ in range(size):
            current_word = q.popleft()
            if current_word == endWord:
                return steps

            word_chars = list(current_word)
            for i in range(len(word_chars)):
                original_char = word_chars[i]
                for j in range(26):
                    word_chars[i] = chr(ord('a') + j)
                    new_word = ''.join(word_chars)
                    if new_word in word_set:
                        q.append(new_word)
                        current_level.add(new_word)
                        
                word_chars[i] = original_char
        
        word_set -= current_level
        steps += 1
        
    return 0

## Structure
from collections import deque
    # Your code here

    pass