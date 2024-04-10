##Question ID: 1184

def carPooling(trips, capacity):
    stops = [0] * 1001
    for num, start, end in trips:
        stops[start] += num
        stops[end] -= num
    for i in stops:
        capacity -= i
        if capacity < 0:
            return False
    return True

## Structure
def carPooling(trips, capacity):
    # Your code here

    pass