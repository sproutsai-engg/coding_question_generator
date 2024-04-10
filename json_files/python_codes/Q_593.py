##Question ID: 593

def validSquare(p1, p2, p3, p4):
    def dist_sq(p, q):
        return (p[0] - q[0])**2 + (p[1] - q[1])**2

    points = [p1, p2, p3, p4]
    dists = set()

    for i in range(4):
        for j in range(i + 1, 4):
            dists.add(dist_sq(points[i], points[j]))

    return len(dists) == 2 and 0 not in dists

## Structure
def validSquare(p1, p2, p3, p4):
    # Your code here

    pass