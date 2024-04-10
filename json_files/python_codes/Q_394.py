##Question ID: 394

def decodeString(s):
    counts = []
    results = []
    current = ""
    ptr = 0

    while ptr < len(s):
        if s[ptr].isdigit():
            count = 0
            while s[ptr].isdigit():
                count = count * 10 + int(s[ptr])
                ptr += 1
            counts.append(count)
        elif s[ptr] == '[':
            results.append(current)
            current = ""
            ptr += 1
        elif s[ptr] == ']':
            prev = results.pop()
            count = counts.pop()
            current = prev + current * count
            ptr += 1
        else:
            current += s[ptr]
            ptr += 1

    return current

## Structure
def decodeString(s):
    # Your code here

    pass