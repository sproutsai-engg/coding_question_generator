##Question ID: 699

def fallingSquares(positions):
    ans = []
    intervals = []

    for p in positions:
        L, size = p
        R = L + size
        h = size
        for h2, R2 in intervals:
            if R2 > L and R > R2:
                h = max(h, size + h2)

        maxHeight = max((h2 for h2, R2 in intervals), default=0)
        ans.append(max(maxHeight, h))
        intervals.append((h, R))

    return ans

## Structure
def fallingSquares(positions):
    # Your code here

    pass