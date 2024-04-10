##Question ID: 159

def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    l, r, max_len, cur_len = 0, 0, 0, 0
    char_count = {}

    while r < len(s):
        if s[r] in char_count:
            char_count[s[r]] += 1
        else:
            char_count[s[r]] = 1
        if len(char_count) <= 2:
            cur_len += 1
        else:
            while len(char_count) > 2 and l <= r:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1
                cur_len -= 1
            cur_len += 1
        max_len = max(max_len, cur_len)
        r += 1
    return max_len

## Structure
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    # Your code here

    pass