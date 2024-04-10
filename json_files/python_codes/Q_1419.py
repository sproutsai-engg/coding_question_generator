##Question ID: 1419

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    counter = [0] * 5
    frogs = max_frogs = 0
    for ch in croakOfFrogs:
        idx = 'croak'.index(ch)
        counter[idx] += 1
        if idx == 0:
            max_frogs = max(max_frogs, frogs + 1)
            frogs += 1
        else:
            counter[idx - 1] -= 1
            if counter[idx - 1] < 0:
                return -1
            if idx == 4:
                frogs -= 1
    return max_frogs if all(count == counter[0] for count in counter) else -1

## Structure
def minNumberOfFrogs(croakOfFrogs: str) -> int:
    # Your code here

    pass