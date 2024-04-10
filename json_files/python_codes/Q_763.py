##Question ID: 763

def partition_labels(s):
    last = {c:i for i, c in enumerate(s)}
    ans = []
    j = anchor = 0
    for i, c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
    return ans

## Structure
def partition_labels(s):
    # Your code here

    pass