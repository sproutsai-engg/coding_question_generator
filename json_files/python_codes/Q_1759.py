##Question ID: 1759

def count_homogenous(s: str) -> int:
    MOD = 1000000007
    count, total = 1, 0
    for i in range(1, len(s)):
        count = count + 1 if s[i] == s[i - 1] else 1
        total = (total + count) % MOD
    return (total + count) % MOD

## Structure
def count_homogenous(s: str) -> int:
    # Your code here

    pass