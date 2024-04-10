##Question ID: 1180

def count_letters(s: str) -> int:
    count = 0
    current = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current += 1
        else:
            count += (current * (current + 1)) // 2
            current = 1

    count += (current * (current + 1)) // 2
    return count

## Structure
def count_letters(s: str) -> int:
    # Your code here

    pass