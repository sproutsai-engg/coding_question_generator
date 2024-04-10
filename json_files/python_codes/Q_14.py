##Question ID: 14

def longest_common_prefix(strs):
    if not strs:
        return ""

    for i, c in enumerate(strs[0]):
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]
    return strs[0]

## Structure
def longest_common_prefix(strs):
    # Your code here

    pass