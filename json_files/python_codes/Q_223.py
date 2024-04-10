##Question ID: 223

def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)

    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return area1 + area2 - overlap_area


## Structure
def total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    # Your code here

    pass