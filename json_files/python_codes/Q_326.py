##Question ID: 326

def is_power_of_three(n: int) -> bool:
    if n < 1:
        return False
    
    while n % 3 == 0:
        n //= 3
    
    return n == 1

## Structure
def is_power_of_three(n: int) -> bool:
    # Your code here

    pass