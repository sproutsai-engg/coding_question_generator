##Question ID: 526

def countArrangement(n: int) -> int:
    def helper(idx: int, visited: List[bool], n: int) -> int:
        if idx > n:
            return 1

        count = 0
        for i in range(1, n+1):
            if not visited[i] and (idx % i == 0 or i % idx == 0):
                visited[i] = True
                count += helper(idx+1, visited, n)
                visited[i] = False

        return count

    visited = [False] * (n+1)
    return helper(1, visited, n)

## Structure
def countArrangement(n: int) -> int:
    # Your code here

    pass