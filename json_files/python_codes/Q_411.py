##Question ID: 411

def abbreviate(s, k, i):
    if i == len(s):
        return str(k) if k > 0 else ""
    if k == 0:
        return s[i:] + (abbreviate(s, 1, i + 1) if i + 1 < len(s) else "")
    return str(k) + s[i] + (abbreviate(s, 1, i + 1) if i + 1 < len(s) else "")

def is_abbreviation(target, word):
    i, j = 0, 0
    while i < len(target) and j < len(word):
        if target[i] == word[j]:
            i, j = i + 1, j + 1
        elif target[i].isdigit():
            k = 0
            while i < len(target) and target[i].isdigit():
                k = k * 10 + int(target[i])
                i += 1
            j += k
        else:
            return False
    return i == len(target) and j == len(word)

def min_abbreviation(target, dictionary):
    ans = target
    for k in range(0, len(target) + 1):
        for i in range(0, len(target) - k + 1):
            current = abbreviate(target, k, i)
            if len(current) < len(ans):
                valid = True
                for word in dictionary:
                    if is_abbreviation(current, word):
                        valid = False
                        break
                if valid:
                    ans = current
    return ans


## Structure
def abbreviate(s, k, i):
    # Your code here

    pass