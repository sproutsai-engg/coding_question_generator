##Question ID: 954

def canReorderDoubled(arr):
    count = collections.Counter(arr)
    
    for a in sorted(count, key=abs):
        if count[a] > 0:
            target = a * 2
            if count[target] < count[a]:
                return False
            count[target] -= count[a]

    return True

## Structure
def canReorderDoubled(arr):
    # Your code here

    pass