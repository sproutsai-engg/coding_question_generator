##Question ID: 1446

def angleClock(hour: int, minutes: int) -> float:
    minute_angle = 6 * minutes
    hour_angle = 30 * hour + 0.5 * minutes
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)

## Structure
def angleClock(hour: int, minutes: int) -> float:
    # Your code here

    pass