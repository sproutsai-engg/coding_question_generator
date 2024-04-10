##Question ID: 1122

def longest_dup_substring(s):
    n = len(s)
    longest_duplicate = ""
    for length in range(n - 1, 0, -1):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if s.find(substring, i + 1) != -1:
                longest_duplicate = substring
                return longest_duplicate
    return longest_duplicate


## Structure
def longest_dup_substring(s):
    # Your code here

    pass