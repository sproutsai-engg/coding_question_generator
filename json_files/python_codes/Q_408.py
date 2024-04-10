##Question ID: 408

def validWordAbbreviation(word, abbr):
    i, j = 0, 0
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == '0': return False  # leading zero
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if word[i] != abbr[j]: return False
            i, j = i + 1, j + 1
    return i == len(word) and j == len(abbr)

## Structure
def validWordAbbreviation(word, abbr):
    # Your code here

    pass