##Question ID: 1689

def containsPattern(arr, m, k):
    n = len(arr)
    if m * k > n:
        return False

    for i in range(n - m * k + 1):
        patternFound = True
        for j in range(m):
            for l in range(1, k):
                if arr[i + j] != arr[i + j + l * m]:
                    patternFound = False
                    break
            if not patternFound:
                break
        if patternFound:
            return True
    return False

## Structure
def containsPattern(arr, m, k):
    # Your code here

    pass