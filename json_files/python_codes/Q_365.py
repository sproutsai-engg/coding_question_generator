##Question ID: 365

def canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity):
    if targetCapacity > jug1Capacity + jug2Capacity:
        return False
    if jug1Capacity == targetCapacity or jug2Capacity == targetCapacity or jug1Capacity + jug2Capacity == targetCapacity:
        return True
    return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


## Structure
def canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity):
    # Your code here

    pass