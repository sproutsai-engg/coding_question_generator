##Question ID: 905

def lenLongestFibSubseq(arr):
    index = {x: i for i, x in enumerate(arr)}

    longest = dict()
    ans = 0

    for k, z in enumerate(arr):
        for j, y in enumerate(arr[:k]):
            i = index.get(z - y, None)
            if i is not None and i < j:
                longest[j, k] = longest.get((i, j), 1) + 1
                ans = max(ans, longest[j, k] + 1)

    return ans if ans >= 3 else 0

## Structure
def lenLongestFibSubseq(arr):
    # Your code here

    pass