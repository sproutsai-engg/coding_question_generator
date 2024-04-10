##Question ID: 305

def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    def index(x: int, y: int) -> int:
        return x * n + y
    
    def find(x: int) -> int:
        if roots[x] != x:
            roots[x] = find(roots[x])
        return roots[x]

    roots = [-1] * (m * n)
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    islandCount = 0
    result = []

    for i, j in positions:
        idx = index(i, j)
        if roots[idx] != -1:
            result.append(islandCount)
            continue
        islandCount += 1
        roots[idx] = idx
        for dx, dy in dirs:
            ni, nj = i + dx, j + dy
            neighbor = index(ni, nj)
            if 0 <= ni < m and 0 <= nj < n and roots[neighbor] != -1:
                root_neighbor = find(neighbor)
                if idx != root_neighbor:
                    roots[root_neighbor] = idx
                    islandCount -= 1
        result.append(islandCount)
    return result


## Structure
def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    # Your code here

    pass