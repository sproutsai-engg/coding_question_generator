##Question ID: 395

def longestSubstring(s: str, k: int) -> int:
    if not s or k <= 0:
        return 0

    char_count = {}
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1

    for char, count in char_count.items():
        if count < k:
            return max(longestSubstring(sub_s, k) for sub_s in s.split(char))
    return len(s)

## Structure
def longestSubstring(s: str, k: int) -> int:
    # Your code here

    pass