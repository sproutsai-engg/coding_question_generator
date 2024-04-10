##Question ID: 1688

def numberOfMatches(n: int) -> int:
    matches = 0
    while n > 1:
        matches += n // 2
        n = (n + 1) // 2
    return matches

## Structure
def numberOfMatches(n: int) -> int:
    # Your code here

    pass