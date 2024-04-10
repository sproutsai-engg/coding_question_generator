##Question ID: 1292

def maxSideLength(mat: List[List[int]], threshold: int) -> int:
    m, n = len(mat), len(mat[0])
    preSum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            preSum[i][j] = mat[i - 1][j - 1] + preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1]

    maxSide = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, min(m, n) + 1):
                endX, endY = i + k - 1, j + k - 1
                if endX <= m and endY <= n:
                    sum = preSum[endX][endY] - preSum[endX][j - 1] - preSum[i - 1][endY] + preSum[i - 1][j - 1]
                    if sum <= threshold:
                        maxSide = max(maxSide, k)
                else:
                    break
    return maxSide


## Structure
def maxSideLength(mat: List[List[int]], threshold: int) -> int:
    # Your code here

    pass