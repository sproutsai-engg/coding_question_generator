##Question ID: 989

from collections import defaultdict

def largestComponentSize(nums):
    def primes(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i
        return n

    def dfs(node, visited, graph):
        if node in visited:
            return 0
        visited.add(node)
        size = 1
        for neighbor in graph[node]:
            size += dfs(neighbor, visited, graph)
        return size

    graph = defaultdict(set)
    visited = set()

    for num in nums:
        prime = primes(num)
        graph[prime].add(num)
        if num != prime:
            graph[num].add(prime)

    count = 0
    for num in nums:
        count = max(count, dfs(num, visited, graph))

    return count

## Structure
from collections import defaultdict
    # Your code here

    pass