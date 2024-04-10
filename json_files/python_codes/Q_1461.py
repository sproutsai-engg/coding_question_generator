##Question ID: 1461

def countOrders(n: int) -> int:
    MOD = 10**9 + 7
    ans = 1
    for i in range(1, n + 1):
        ans = ans * (2 * i - 1) * i % MOD
    return ans

## Structure
def countOrders(n: int) -> int:
    # Your code here

    pass