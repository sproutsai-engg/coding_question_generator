##Question ID: 1534

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    counts = [0] * 5
    max_frogs = 0

    for c in croakOfFrogs:
        index = "croak".find(c)
        if index == 0:
            counts[0] += 1
            max_frogs = max(max_frogs, counts[0])
        elif counts[index - 1] > 0:
            counts[index - 1] -= 1
            counts[index] += 1
        else:
            return -1

    if counts[0] == counts[4]:
        return max_frogs
    else:
        return -1

## Structure
def minNumberOfFrogs(croakOfFrogs: str) -> int:
    # Your code here

    pass