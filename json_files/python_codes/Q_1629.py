##Question ID: 1629

def minInteger(num: str, k: int) -> str:
    if k == 0:
        return num
    num = list(num)
    n = len(num)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if j - i > k:
                break
            if num[j] < num[idx]:
                idx = j
        min_digit = num[idx]
        for j in range(idx, i, -1):
            num[j] = num[j - 1]
        num[i] = min_digit
        k -= idx - i
    return ''.join(num)

## Structure
def minInteger(num: str, k: int) -> str:
    # Your code here

    pass