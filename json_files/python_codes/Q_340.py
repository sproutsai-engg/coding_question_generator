##Question ID: 340

def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    char_count = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

## Structure
def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    # Your code here

    pass