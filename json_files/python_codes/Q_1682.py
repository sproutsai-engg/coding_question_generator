##Question ID: 1682

def most_visited(n, rounds):
    visited = [0] * (n + 1)
    
    for i in range(1, len(rounds)):
        start, end = rounds[i - 1], rounds[i]
        while start != end:
            visited[start] += 1
            start = (start % n) + 1
    visited[rounds[-1]] += 1
    
    max_visits = max(visited);
    return [i for i in range(1, n + 1) if visited[i] == max_visits]

## Structure
def most_visited(n, rounds):
    # Your code here

    pass