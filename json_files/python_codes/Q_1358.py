##Question ID: 1358

def find_pairs(z):
    pairs = []
    
    def f(x, y):
        return x + y
    
    for x in range(1, z+1):
        for y in range(1, z+1):
            if f(x, y) == z:
                pairs.append((x, y))
    return pairs

## Structure
def find_pairs(z):
    # Your code here

    pass