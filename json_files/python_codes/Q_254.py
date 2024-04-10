##Question ID: 254

def getFactors(n):
    def helper(n, start, path, result):
        if n == 1:
            if len(path) > 1:
                result.append(path[:])
            return

        for i in range(start, n + 1):
            if n % i == 0:
                path.append(i)
                helper(n // i, i, path, result)
                path.pop()

    result = []
    helper(n, 2, [], result)
    return result

## Structure
def getFactors(n):
    # Your code here

    pass