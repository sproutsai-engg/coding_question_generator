##Question ID: 1361

def tilingRectangle(n, m):
    if n > m:
        n, m = m, n
    if n == 1:
        return m
    if n == m:
        return 1

    res = float('inf')
    for a in range(1, n // 2 + 1):
        res = min(res, tilingRectangle(a, m) + tilingRectangle(n - a, m))

    for b in range(1, m // 2 + 1):
        res = min(res, tilingRectangle(n, b) + tilingRectangle(n, m - b))

    return res


## Structure
def tilingRectangle(n, m):
    # Your code here

    pass