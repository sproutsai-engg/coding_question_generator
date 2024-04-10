##Question ID: 1210

def trimmed_mean(arr):
    n = len(arr)
    remove = int(n * 0.05)
    arr.sort()
    return sum(arr[remove:n - remove]) / (n - 2 * remove)

## Structure
def trimmed_mean(arr):
    # Your code here

    pass