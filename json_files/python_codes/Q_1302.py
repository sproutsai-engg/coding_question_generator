##Question ID: 1302

def make_fancy_string(s: str) -> str:
    result = [s[0]]
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            count = 1
        if count < 3:
            result.append(s[i])

    return ''.join(result)


## Structure
def make_fancy_string(s: str) -> str:
    # Your code here

    pass