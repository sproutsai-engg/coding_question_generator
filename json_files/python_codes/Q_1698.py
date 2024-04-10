##Question ID: 1698

def modifyString(s: str) -> str:
    s = list(s)
    for i in range(len(s)):
        if s[i] == '?':
            for c in range(ord('a'), ord('z') + 1):
                if (i - 1 < 0 or s[i - 1] != chr(c)) and (i + 1 >= len(s) or s[i + 1] != chr(c)):
                    s[i] = chr(c)
                    break
    return ''.join(s)


## Structure
def modifyString(s: str) -> str:
    # Your code here

    pass