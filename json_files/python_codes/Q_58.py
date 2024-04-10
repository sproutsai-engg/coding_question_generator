##Question ID: 58

def length_of_last_word(s: str) -> int:
    length = 0
    tail = len(s) - 1
    while tail >= 0 and s[tail] == ' ':
        tail -= 1
    while tail >= 0 and s[tail] != ' ':
        length += 1
        tail -= 1
    return length

## Structure
def length_of_last_word(s: str) -> int:
    # Your code here

    pass