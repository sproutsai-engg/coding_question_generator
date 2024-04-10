##Question ID: 1028

def interval_intersection(firstList, secondList):
    result = []
    i, j = 0, 0

    while i < len(firstList) and j < len(secondList):
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])

        if start <= end:
            result.append([start, end])

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return result

## Structure
def interval_intersection(firstList, secondList):
    # Your code here

    pass