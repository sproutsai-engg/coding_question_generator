##Question ID: 447

def numberOfBoomerangs(points):
    count = 0

    for i in points:
        group_count = {}
        for j in points:
            dx, dy = i[0] - j[0], i[1] - j[1]
            dist = dx * dx + dy * dy
            group_count[dist] = group_count.get(dist, 0) + 1

        for g in group_count.values():
            count += g * (g - 1)

    return count

## Structure
def numberOfBoomerangs(points):
    # Your code here

    pass