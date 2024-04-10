##Question ID: 1585

def kth_factor(n: int, k: int) -> int:
    for i in range(1, n+1):
        if n % i == 0:
            k -= 1
            if k == 0:
                return i
    return -1


## Structure
def kth_factor(n: int, k: int) -> int:
    # Your code here

    pass