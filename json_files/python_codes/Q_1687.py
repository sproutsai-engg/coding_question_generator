##Question ID: 1687

def min_trips(boxes, portsCount, maxBoxes, maxWeight):
    trips = 0
    idx = 0
    n = len(boxes)
    while idx < n:
        curr_limit = maxWeight
        prev_port = 0
        count = 0
        while count < maxBoxes and idx < n:
            if boxes[idx][1] <= curr_limit:
                if prev_port != boxes[idx][0]:
                    prev_port = boxes[idx][0]
                    trips += 1
                curr_limit -= boxes[idx][1]
                count += 1
                idx += 1
            else:
                break
        trips += 1
    return trips

## Structure
def min_trips(boxes, portsCount, maxBoxes, maxWeight):
    # Your code here

    pass