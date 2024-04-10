##Question ID: 1183

def sampleStats(count):
    minVal, maxVal, mode, median, mean = -1, -1, 0, 0, 0
    totalCount, modeCount, curCount = 0, 0, 0
    sum = 0

    for i in range(256):
        if count[i] > 0:
            if minVal == -1:
                minVal = i
            maxVal = i
            sum += i * count[i]
            totalCount += count[i]
            if count[i] > modeCount:
                modeCount = count[i]
                mode = i

    mean = sum / totalCount
    isEven = (totalCount % 2 == 0)
    mid1 = totalCount // 2
    mid2 = mid1 - 1
    if isEven:
        mid2 += 1

    for i in range(256):
        curCount += count[i]
        if isEven and curCount >= mid2:
            median += i
            mid2 = totalCount
            isEven = False

        if curCount >= mid1:
            median += i
            break

    if not isEven:
        median /= 2
    return [minVal, maxVal, mean, median, mode]

## Structure
def sampleStats(count):
    # Your code here

    pass