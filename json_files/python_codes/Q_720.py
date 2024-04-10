##Question ID: 720

def longest_word(words):
    built_words = set()
    result = ''

    for word in sorted(words):
        if len(word) == 1 or word[:-1] in built_words:
            if len(word) > len(result):
                result = word
            built_words.add(word)

    return result


## Structure
def longest_word(words):
    # Your code here

    pass