##Question ID: 1007

def numsSameConsecDiff(n, k):
    result = []
    if n == 1: result.append(0)

    def dfs(current):
        if len(current) == n:
            result.append(int(current))
            return

        last_digit = current[-1]
        if last_digit - k >= 0: dfs(current + str(last_digit - k))
        if k != 0 and last_digit + k <= 9: dfs(current + str(last_digit + k))

    for i in range(1, 10):
        dfs(str(i))

    return result

## Structure
def numsSameConsecDiff(n, k):
    # Your code here

    pass