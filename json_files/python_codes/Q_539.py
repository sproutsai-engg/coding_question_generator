##Question ID: 539

def findMinDifference(timePoints):
    timePoints.sort()
    min_difference = float('inf')

    for i in range(len(timePoints)):
        h1, m1 = map(int, timePoints[i].split(':'))
        h2, m2 = map(int, timePoints[(i+1)%len(timePoints)].split(':'))
        cur_difference = abs((h1 * 60 + m1) - (h2 * 60 + m2))
        min_difference = min(min_difference, 1440 - cur_difference if cur_difference > 720 else cur_difference)

    return min_difference

## Structure
def findMinDifference(timePoints):
    # Your code here

    pass