##Question ID: 1244

def num_distinct_repeated_substrings(s):
    seen = set()
    for length in range(len(s) // 2, 0, -1):
        for i in range(len(s) - 2 * length + 1):
            substr = s[i:i + length]
            if substr in s[i + length:]:
                seen.add(substr)
    return len(seen)


## Structure
def num_distinct_repeated_substrings(s):
    # Your code here

    pass