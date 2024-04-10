##Question ID: 1039

def find_judge(n, trust):
    trustCounts = [0] * (n + 1)
    for a, b in trust:
        trustCounts[a] -= 1
        trustCounts[b] += 1

    for i in range(1, n + 1):
        if trustCounts[i] == n - 1:
            return i
    return -1

## Structure
def find_judge(n, trust):
    # Your code here

    pass