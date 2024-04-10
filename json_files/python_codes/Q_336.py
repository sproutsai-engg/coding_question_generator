##Question ID: 336

def palindrome_pairs(words):
    def is_palindrome(s):
        return s == s[::-1]

    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            concat = words[i] + words[j]
            if is_palindrome(concat):
                result.append([i, j])
    return result

## Structure
def palindrome_pairs(words):
    # Your code here

    pass