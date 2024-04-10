##Question ID: 1404

def num_steps(s: str) -> int:
    steps = 0
    carry = 0
    
    for c in reversed(s[1:]):
        bit = int(c)
        if bit and carry:
            carry = 1
            steps += 2
        elif bit or carry:
            carry ^= 1
            steps += 2
        else:
            steps += 1
            
    return steps + carry

## Structure
def num_steps(s: str) -> int:
    # Your code here

    pass