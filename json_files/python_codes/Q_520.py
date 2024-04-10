##Question ID: 520

def detectCapitalUse(word: str) -> bool:
    numCapital = sum(1 for c in word if c.isupper())
    return numCapital == 0 or numCapital == len(word) or (numCapital == 1 and word[0].isupper())


## Structure
def detectCapitalUse(word: str) -> bool:
    # Your code here

    pass