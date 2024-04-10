##Question ID: 1696

def isPrintable(targetGrid):
    m, n = len(targetGrid), len(targetGrid[0])
    top, bottom, left, right = [m]*61, [-1]*61, [n]*61, [-1]*61
    vis = [[False]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            c = targetGrid[i][j]
            top[c] = min(top[c], i)
            bottom[c] = max(bottom[c], i)
            left[c] = min(left[c], j)
            right[c] = max(right[c], j)

    def dfs(x):
        i, j = x // n, x % n
        if vis[i][j]: return True
        c = targetGrid[i][j]
        if i < top[c] or i > bottom[c] or j < left[c] or j > right[c]: return False
        vis[i][j] = True
        for k in range(1, 61):
            if k == c: continue
            if i >= top[k] and i <= bottom[k] and j >= left[k] and j <= right[k]: return False
            if not dfs(((i-top[k])*(right[k]-left[k]+1)) + j - left[k]): return False
        return True

    for color in range(1, 61):
        for i in range(top[color], bottom[color] + 1):
            for j in range(left[color], right[color] + 1):
                if not vis[i][j] and not dfs(i * n + j): return False

    return True


## Structure
def isPrintable(targetGrid):
    # Your code here

    pass