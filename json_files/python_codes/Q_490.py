##Question ID: 490

def hasPath(maze, start, destination):
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    q = [start]
    while q:
        x, y = q.pop(0)
        if x == destination[0] and y == destination[1]:
            return True
        for dx, dy in dirs:
            i, j = x, y
            while 0 <= i + dx < len(maze) and 0 <= j + dy < len(maze[0]) and maze[i + dx][j + dy] == 0:
                i += dx
                j += dy
            if maze[i][j] == 0:
                maze[i][j] = 1
                q.append((i, j))
    return False

## Structure
def hasPath(maze, start, destination):
    # Your code here

    pass