##Question ID: 1761

def count_vowel_strings(n):
    dp = [1, 1, 1, 1, 1]

    for i in range(1, n):
        for j in range(3, -1, -1):
            dp[j] += dp[j + 1]

    return sum(dp)

## Structure
def count_vowel_strings(n):
    # Your code here

    pass