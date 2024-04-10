##Question ID: 1106

MAX_STEPS = 200

def isEscapePossible(blocked, source, target):
    blockedSet = set(["{}_{}".format(block[0], block[1]) for block in blocked])
    visited = set()

    def dfs(x, y, tx, ty, steps):
        pos = "{}_{}".format(x, y)
        if x < 0 or x >= 1000000 or y < 0 or y >= 1000000 or steps >= MAX_STEPS or pos in blockedSet or pos in visited:
            return False

        if x == tx and y == ty:
            return True

        visited.add(pos)

        return (dfs(x + 1, y, tx, ty, steps + 1) or dfs(x, y + 1, tx, ty, steps + 1)
                or dfs(x - 1, y, tx, ty, steps + 1) or dfs(x, y - 1, tx, ty, steps + 1))

    return dfs(source[0], source[1], target[0], target[1], 0)


## Structure
MAX_STEPS = 200
    # Your code here

    pass