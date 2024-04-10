##Question ID: 1444

def number_of_steps(num):
    steps = 0
    while num:
        steps += 1 if num % 2 == 0 else 2
        num >>= 1
    return steps - 1

## Structure
def number_of_steps(num):
    # Your code here

    pass