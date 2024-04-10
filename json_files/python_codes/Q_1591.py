##Question ID: 1591

def isPrintable(self, targetGrid: List[List[int]]) -> bool:
    color_bounds = {}
    m, n = len(targetGrid), len(targetGrid[0])

    for i in range(m):
        for j in range(n):
            color = targetGrid[i][j]
            if color not in color_bounds:
                color_bounds[color] = [i, j, i, j]
            else:
                color_bounds[color][0] = min(color_bounds[color][0], i)
                color_bounds[color][1] = min(color_bounds[color][1], j)
                color_bounds[color][2] = max(color_bounds[color][2], i)
                color_bounds[color][3] = max(color_bounds[color][3], j)

    remaining_colors = set(color_bounds.keys())
    while remaining_colors:
        progress = False
        to_remove = set()
        for color in remaining_colors:
            bounds = color_bounds[color]
            contained = all(targetGrid[i][j] == color or targetGrid[i][j] == -1
                        for i in range(bounds[0], bounds[2] + 1)
                        for j in range(bounds[1], bounds[3] + 1))
            if contained:
                for i in range(bounds[0], bounds[2] + 1):
                    for j in range(bounds[1], bounds[3] + 1):
                        targetGrid[i][j] = -1
                to_remove.add(color)
                progress = True

        remaining_colors -= to_remove
        if not progress:
            return False

    return True


## Structure
def isPrintable(self, targetGrid: List[List[int]]) -> bool:
    # Your code here

    pass