##Question ID: 670

def maximumSwap(num):
    num_str = list(str(num))
    last = {int(v): i for i, v in enumerate(num_str)}

    for i, v in enumerate(num_str):
        for d in range(9, int(v), -1):
            if last.get(d, -1) > i:
                num_str[i], num_str[last[d]] = num_str[last[d]], num_str[i]
                return int("".join(num_str))

    return num

## Structure
def maximumSwap(num):
    # Your code here

    pass