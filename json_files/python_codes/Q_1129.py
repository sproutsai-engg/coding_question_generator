##Question ID: 1129

def longestStrChain(words):
    words.sort(key=lambda x: len(x))
    dp = {}

    max_len = 0
    for word in words:
        for i in range(len(word)):
            pre = word[:i] + word[i + 1:]
            dp[word] = max(dp.get(word, 0), dp.get(pre, 0) + 1)
        max_len = max(max_len, dp[word])

    return max_len

## Structure
def longestStrChain(words):
    # Your code here

    pass