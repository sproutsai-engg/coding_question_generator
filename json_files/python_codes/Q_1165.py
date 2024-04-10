##Question ID: 1165

def calculate_time(keyboard: str, word: str) -> int:
    time = 0
    prev_index = 0
    char_to_index = {char: i for i, char in enumerate(keyboard)}

    for c in word:
        time += abs(char_to_index[c] - prev_index)
        prev_index = char_to_index[c]

    return time

## Structure
def calculate_time(keyboard: str, word: str) -> int:
    # Your code here

    pass