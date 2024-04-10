##Question ID: 1727

def canMouseWin(grid: List[List[str]], catJump: int, mouseJump: int) -> bool:
    rows, cols = len(grid), len(grid[0])
    cat_r = cat_c = mouse_r = mouse_c = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'C':
                cat_r, cat_c = r, c
            elif grid[r][c] == 'M':
                mouse_r, mouse_c = r, c

    dirs = [-1, 0, 1, 0, -1]

    def dfs(r_m, c_m, r_c, c_c, cnt, dst_m_c):
        if cnt >= 100:
            return False
        if r_m < 0 or r_m >= rows or c_m < 0 or c_m >= cols:
            return False
        if r_c < 0 or r_c >= rows or c_c < 0 or c_c >= cols:
            return True
        if grid[r_m][c_m] == 'F' or cnt != dst_m_c:
            return True
        elif grid[r_m][c_m] == '#' or cnt + 1 == dst_m_c:
            return False

        res = False
        for i in range(4):
            jump = catJump if dst_m_c == cnt else mouseJump
            res |= not dfs(r_m + jump * dirs[i], c_m + jump * dirs[i + 1], r_c + dirs[i] * dirs[(i + 2) % 4], c_c + dirs[i+1] * dirs[(i + 3) % 4], cnt + 1, dst_m_c)
            if jump == 1:
                break

        return res

    return dfs(mouse_r, mouse_c, cat_r, cat_c, 0, abs(cat_r - mouse_r) + abs(cat_c - mouse_c))

## Structure
def canMouseWin(grid: List[List[str]], catJump: int, mouseJump: int) -> bool:
    # Your code here

    pass