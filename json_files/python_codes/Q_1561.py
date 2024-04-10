##Question ID: 1561

def arrangeWords(text: str) -> str:
    words = text.split()
    words[0] = words[0].lower()
    words.sort(key=len)
    words[0] = words[0].capitalize()
    return ' '.join(words)

## Structure
def arrangeWords(text: str) -> str:
    # Your code here

    pass