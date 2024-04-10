##Question ID: 351

def numberOfPatterns(m: int, n: int) -> int:
    def dfs(curr, remaining):
        if remaining < 0:
            return 0
        if remaining == 0:
            return 1

        visited[curr] = True
        cnt = 0
        for next in range(1, 10):
            if not visited[next] and (jumps[curr][next] == 0 or visited[jumps[curr][next]]):
                cnt += dfs(next, remaining - 1)
        visited[curr] = False

        return cnt

    jumps = [[0] * 10 for _ in range(10)]
    jumps[1][3] = jumps[3][1] = 2
    jumps[1][7] = jumps[7][1] = 4
    jumps[3][9] = jumps[9][3] = 6
    jumps[7][9] = jumps[9][7] = 8
    jumps[1][9] = jumps[9][1] = jumps[2][8] = jumps[8][2] = jumps[3][7] = jumps[7][3] = jumps[4][6] = jumps[6][4] = 5

    visited = [False] * 10

    cnt = 0
    for i in range(m, n + 1):
        cnt += dfs(1, i - 1) * 4  # 1, 3, 7, 9
        cnt += dfs(2, i - 1) * 4  # 2, 4, 6, 8
        cnt += dfs(5, i - 1)      # 5

    return cnt


## Structure
def numberOfPatterns(m: int, n: int) -> int:
    # Your code here

    pass