##Question ID: 761

def makeLargestSpecial(s: str) -> str:
    count, i = 0, 0
    subs = []

    for j in range(len(s)):
        if s[j] == '1':
            count += 1
        else:
            count -= 1

        if count == 0:
            subs.append("1" + makeLargestSpecial(s[i+1:j]) + "0")
            i = j + 1

    subs.sort(reverse=True)
    return "".join(subs)


## Structure
def makeLargestSpecial(s: str) -> str:
    # Your code here

    pass