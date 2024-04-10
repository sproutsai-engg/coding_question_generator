##Question ID: 976

def min_area_rect(points):
    point_set = {(x, y) for x, y in points}
    min_area = float('inf')

    for p1 in point_set:
        for p2 in point_set:
            if p1[0] != p2[0] and p1[1] != p2[1]:
                if (p1[0], p2[1]) in point_set and (p2[0], p1[1]) in point_set:
                    min_area = min(min_area, abs((p1[0] - p2[0]) * (p1[1] - p2[1])))

    return min_area if min_area != float('inf') else 0


## Structure
def min_area_rect(points):
    # Your code here

    pass