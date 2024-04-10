##Question ID: 475

def findRadius(houses, heaters):
    houses.sort()
    heaters.sort()
    result, i = 0, 0

    for house in houses:
        while i < len(heaters) - 1 and abs(heaters[i + 1] - house) <= abs(heaters[i] - house):
            i += 1
        result = max(result, abs(heaters[i] - house))

    return result

## Structure
def findRadius(houses, heaters):
    # Your code here

    pass