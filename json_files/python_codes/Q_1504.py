##Question ID: 1504

def numSubmat(mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    dp = [[0] * n for _ in range(m)]
    ans = 0
    
    for i in range(m):
        for j in range(n):
            if mat[i][j]:
                dp[i][j] = 1 if j == 0 else dp[i][j-1] + 1
                width = dp[i][j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    ans += width
    
    return ans

## Structure
def numSubmat(mat: List[List[int]]) -> int:
    # Your code here

    pass