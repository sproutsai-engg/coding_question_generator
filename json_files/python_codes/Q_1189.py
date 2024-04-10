##Question ID: 1189

def max_number_of_balloons(text: str) -> int:
    letter_count = [0] * 5
    for c in text:
        if c == 'b': letter_count[0] += 1
        if c == 'a': letter_count[1] += 1
        if c == 'l': letter_count[2] += 1
        if c == 'o': letter_count[3] += 1
        if c == 'n': letter_count[4] += 1
    letter_count[2] //= 2
    letter_count[3] //= 2
    return min(letter_count)

## Structure
def max_number_of_balloons(text: str) -> int:
    # Your code here

    pass