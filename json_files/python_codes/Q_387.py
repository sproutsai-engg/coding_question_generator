##Question ID: 387

def firstUniqChar(s):
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i
    return -1


## Structure
def firstUniqChar(s):
    # Your code here

    pass