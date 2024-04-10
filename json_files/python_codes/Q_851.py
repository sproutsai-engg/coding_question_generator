##Question ID: 851

def to_goat_latin(sentence: str) -> str:
    words = sentence.split()
    vowels = set("AEIOUaeiou")
    result = []

    for i, word in enumerate(words):
        if word[0] not in vowels:
            word = word[1:] + word[0]
        result.append(word + "ma" + "a" * (i + 1))

    return ' '.join(result)

## Structure
def to_goat_latin(sentence: str) -> str:
    # Your code here

    pass