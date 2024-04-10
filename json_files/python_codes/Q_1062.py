##Question ID: 1062

def find_longest_repeating_substring(s: str) -> int:
    n = len(s)
    max_substr_length = 0
    for length in range(1, n // 2 + 1):
        max_repeat_count = repeat_count = 0
        for i in range(n - length):
            if s[i:i + length] == s[i + length:i + 2 * length]:
                repeat_count += 1
            else:
                max_repeat_count = max(max_repeat_count, repeat_count)
                repeat_count = 0
        max_substr_length = max(max_substr_length, max_repeat_count * length)
    return max_substr_length

## Structure
def find_longest_repeating_substring(s: str) -> int:
    # Your code here

    pass