##Question ID: 587

def cross_product(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def fence(trees):
    trees.sort(key=lambda p: (p[0], p[1]))
    hull = []
    for p in trees:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) > 0:
            hull.pop()
        hull.append(p)

    for p in reversed(trees):
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) > 0:
            hull.pop()
        hull.append(p)
    
    return hull

## Structure
def cross_product(p, q, r):
    # Your code here

    pass