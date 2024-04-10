##Question ID: 290

def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    char_map, word_map = {}, {}
    for c, word in zip(pattern, words):
        if c not in char_map and word not in word_map:
            char_map[c] = word
            word_map[word] = c
        else:
            if char_map.get(c) != word or word_map.get(word) != c:
                return False

    return True


## Structure
def word_pattern(pattern, s):
    # Your code here

    pass