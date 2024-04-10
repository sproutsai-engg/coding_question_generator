##Question ID: 1563

from math import acos, cos, sin, sqrt

def max_number_of_darts(darts, r):
    n = len(darts)
    max_darts = 1

    for i in range(n):
        for j in range(i + 1, n):
            dist = sqrt((darts[j][0] - darts[i][0])**2 + (darts[j][1] - darts[i][1])**2)
            if dist > 2.0 * r: continue

            angle = acos(dist / (2.0 * r))
            for k in range(2):
                loc_angle = angle * (1 if k == 0 else -1)
                cx = darts[i][0] + r * (darts[j][0] - darts[i][0]) / dist * cos(loc_angle) - r * (darts[j][1] - darts[i][1]) / dist * sin(loc_angle)
                cy = darts[i][1] + r * (darts[j][0] - darts[i][0]) / dist * sin(loc_angle) + r * (darts[j][1] - darts[i][1]) / dist * cos(loc_angle)

                cnt = 0
                for l in range(n):
                    new_dist = sqrt((darts[l][0] - cx)**2 + (darts[l][1] - cy)**2)
                    if new_dist <= r + 1e-5: cnt += 1

                max_darts = max(max_darts, cnt)

    return max_darts

## Structure
from math import acos, cos, sin, sqrt
    # Your code here

    pass