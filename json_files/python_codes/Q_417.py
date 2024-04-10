##Question ID: 417

def pacificAtlantic(heights):
    def dfs(r, c, prev_height, visited):
        if not (0 <= r < len(heights)) or not (0 <= c < len(heights[0])):
            return
        if heights[r][c] >= prev_height and not visited[r][c]:
            visited[r][c] = True
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)

    m, n = len(heights), len(heights[0])
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]

    for r in range(m):
        dfs(r, 0, -1, pacific)
        dfs(r, n - 1, -1, atlantic)
    for c in range(n):
        dfs(0, c, -1, pacific)
        dfs(m - 1, c, -1, atlantic)

    result = []
    for r in range(m):
        for c in range(n):
            if pacific[r][c] and atlantic[r][c]:
                result.append([r, c])
    return result


## Structure
def pacificAtlantic(heights):
    # Your code here

    pass