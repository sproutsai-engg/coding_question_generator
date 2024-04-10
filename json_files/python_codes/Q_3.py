##Question ID: 3

def length_of_longest_substring(s: str) -> int:
    left = 0
    right = 0
    max_length = 0
    characters = set()

    while right < len(s):
        if s[right] not in characters:
            characters.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            characters.remove(s[left])
            left += 1

    return max_length

## Structure
def length_of_longest_substring(s: str) -> int:
    # Your code here

    pass