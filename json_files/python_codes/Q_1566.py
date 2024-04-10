##Question ID: 1566

def is_prefix_of_word(sentence: str, search_word: str) -> int:
    words = sentence.split(' ')
    for index, word in enumerate(words, start=1):
        if word.startswith(search_word):
            return index
    return -1

## Structure
def is_prefix_of_word(sentence: str, search_word: str) -> int:
    # Your code here

    pass