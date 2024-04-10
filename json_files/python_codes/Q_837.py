##Question ID: 837

def mostCommonWord(paragraph: str, banned: List[str]):
    word_count = {}
    banned_set = {ban.lower() for ban in banned}

    for word in paragraph.lower().split():
        cleaned_word = ''.join(c for c in word if c.isalpha())
        if cleaned_word not in banned_set:
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    return max(word_count, key=word_count.get)


## Structure
def mostCommonWord(paragraph: str, banned: List[str]):
    # Your code here

    pass