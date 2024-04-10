##Question ID: 472

def is_concatenated(word, word_dict):
    n = len(word)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and word[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]


def find_all_concatenated_words(words):
    word_dict = set(words)
    result = []

    for word in words:
        if is_concatenated(word, word_dict):
            result.append(word)

    return result

## Structure
def is_concatenated(word, word_dict):
    # Your code here

    pass