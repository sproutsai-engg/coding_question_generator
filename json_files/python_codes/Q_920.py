##Question ID: 920

def uncommon_from_sentences(s1, s2):
    word_count = {}
    for word in (s1 + " " + s2).split():
        word_count[word] = word_count.get(word, 0) + 1

    return [key for key, val in word_count.items() if val == 1]

## Structure
def uncommon_from_sentences(s1, s2):
    # Your code here

    pass