##Question ID: 1520

def num_steps(s: str) -> int:
    steps = 0
    carry = 0

    for i in range(len(s) - 1, 0, -1):
        current = int(s[i]) + carry
        if current == 1:
            steps += 2
            carry = 1
        else:
            steps += carry
            carry = current

    return steps + carry

## Structure
def num_steps(s: str) -> int:
    # Your code here

    pass