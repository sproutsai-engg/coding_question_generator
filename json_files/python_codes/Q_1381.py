##Question ID: 1381

def get_max_score(word, score):
    return sum(score[ord(c) - ord('a')] for c in word)

def get_max_score_helper(words, score, letters, i):
    if i == len(words):
        return 0
    letters_copy = letters.copy()
    for c in words[i]:
        if letters_copy[c] == 0:
            return get_max_score_helper(words, score, letters, i + 1)
        letters_copy[c] -= 1
    return max(get_max_score(words[i], score) + get_max_score_helper(words, score, letters_copy, i + 1),
               get_max_score_helper(words, score, letters, i + 1))

def max_score_words(words, letters, score):
    letters_count = {}
    for letter in letters:
        letters_count[letter] = letters_count.get(letter, 0) + 1
    return get_max_score_helper(words, score, letters_count, 0)
```
## Structure
def get_max_score(word, score):
    # Your code here

```    pass