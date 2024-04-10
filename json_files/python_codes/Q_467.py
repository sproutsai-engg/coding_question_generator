##Question ID: 467

def findSubstringInWraproundString(p: str) -> int:
    cnt = [0] * 26
    length = 0

    for i in range(len(p)):
        if i > 0 and (p[i] == chr(ord(p[i - 1]) + 1) or ord(p[i - 1]) - ord(p[i]) == 25):
            length += 1
        else:
            length = 1
        cnt[ord(p[i]) - ord('a')] = max(cnt[ord(p[i]) - ord('a')], length)

    return sum(cnt)


## Structure
def findSubstringInWraproundString(p: str) -> int:
    # Your code here

    pass