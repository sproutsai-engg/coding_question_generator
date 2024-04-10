##Question ID: 1751

def slowestKey(releaseTimes, keysPressed):
    max_key = keysPressed[0]
    max_duration = releaseTimes[0]
    for i in range(1, len(releaseTimes)):
        duration = releaseTimes[i] - releaseTimes[i - 1]
        if duration > max_duration or (duration == max_duration and keysPressed[i] > max_key):
            max_key = keysPressed[i]
            max_duration = duration
    return max_key


## Structure
def slowestKey(releaseTimes, keysPressed):
    # Your code here

    pass