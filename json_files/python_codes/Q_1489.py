##Question ID: 1489

def max_size_slices(slices):
    def max_sum(slices, start, end, n, memo):
        if n == 0:
            return 0
        if end - start + 1 < n * 2:
            return float('-inf')
        if memo[start][n] != -1:
            return memo[start][n]

        pick = max_sum(slices, start + 2, end, n - 1, memo) + slices[start]
        not_pick = max_sum(slices, start + 1, end, n, memo)

        memo[start][n] = max(pick, not_pick)
        return memo[start][n]

    n = len(slices) // 3
    memo1 = [[-1] * (n + 1) for _ in range(len(slices))]
    memo2 = [[-1] * (n + 1) for _ in range(len(slices))]

    return max(max_sum(slices, 0, len(slices) - 1, n, memo1),
               max_sum(slices, 1, len(slices), n, memo2))


## Structure
def max_size_slices(slices):
    # Your code here

    pass