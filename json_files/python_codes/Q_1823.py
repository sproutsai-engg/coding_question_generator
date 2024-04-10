##Question ID: 1823

def halves_are_alike(s: str) -> bool:
    half_length = len(s) // 2
    count_a, count_b = 0, 0

    for i in range(half_length):
        if s[i] in "aeiouAEIOU": count_a += 1

    for i in range(half_length, len(s)):
        if s[i] in "aeiouAEIOU": count_b += 1

    return count_a == count_b

## Structure
def halves_are_alike(s: str) -> bool:
    # Your code here

    pass