##Question ID: 438

def find_anagrams(s, p):
    if len(s) < len(p):
        return []

    s_count = [0] * 26
    p_count = [0] * 26
    for c in p:
        p_count[ord(c) - ord('a')] += 1

    result = []
    for i in range(len(s)):
        s_count[ord(s[i]) - ord('a')] += 1
        if i >= len(p):
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1
        if s_count == p_count:
            result.append(i - len(p) + 1)

    return result

## Structure
def find_anagrams(s, p):
    # Your code here

    pass