##Question ID: 186

def reverseWords(s: list) -> None:
    def reverse(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    reverse(s, 0, len(s)-1)
    start = 0
    for i, char in enumerate(s + [' ']):
        if char == ' ':
            reverse(s, start, i - 1)
            start = i + 1

## Structure
def reverseWords(s: list) -> None:
    # Your code here

    pass