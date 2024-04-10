##Question ID: 1833

def largestAltitude(gain):
    max_altitude, current_altitude = 0, 0
    for i in gain:
        current_altitude += i
        max_altitude = max(max_altitude, current_altitude)
    return max_altitude

## Structure
def largestAltitude(gain):
    # Your code here

    pass