##Question ID: 60

def getPermutation(n, k):
    factorials = [1]
    nums = list(range(1, n + 1))
    result = []

    for i in range(1, n):
        factorials.append(factorials[-1] * i)

    k -= 1

    for i in range(n, 0, -1):
        index = k // factorials[i - 1]
        k %= factorials[i - 1]
        result.append(str(nums.pop(index)))

    return ''.join(result)

## Structure
def getPermutation(n, k):
    # Your code here

    pass