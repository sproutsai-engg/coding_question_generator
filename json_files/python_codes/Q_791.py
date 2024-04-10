##Question ID: 791

def customSortString(order, s):
    priority = {char: idx for idx, char in enumerate(order)}
    return "".join(sorted(s, key=lambda x: priority.get(x, 0)))

## Structure
def customSortString(order, s):
    # Your code here

    pass