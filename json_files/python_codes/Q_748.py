##Question ID: 748

def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    from collections import Counter

    lp_count = Counter(c.lower() for c in licensePlate if c.isalpha())

    result = ""
    for word in words:
        word_count = Counter(word)

        valid = all(word_count[ch] >= count for ch, count in lp_count.items())

        if valid and (not result or len(word) < len(result)):
            result = word

    return result


## Structure
def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    # Your code here

    pass