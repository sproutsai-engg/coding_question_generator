##Question ID: 1620

def canArrange(arr, k):
    counts = [0] * k
    for num in arr:
        counts[(num % k + k) % k] += 1
    if counts[0] % 2 != 0:
        return False
    for i in range(1, k // 2 + 1):
        if counts[i] != counts[k - i]:
            return False
    return True

## Structure
def canArrange(arr, k):
    # Your code here

    pass