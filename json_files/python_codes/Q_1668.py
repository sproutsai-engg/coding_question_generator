##Question ID: 1668

def longestAwesomeSubstring(s):
    n = len(s)
    maxLen = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if isAwesome(substr):
                maxLen = max(maxLen, j - i)
    return maxLen

def isAwesome(s):
    odd_count = 0
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    for i in range(26):
        if freq[i] % 2 == 1:
            odd_count += 1
    return odd_count <= 1

## Structure
def longestAwesomeSubstring(s):
    # Your code here

    pass