##Question ID: 852

def numFriendRequests(ages):
    count = [0] * 121
    total_requests = 0

    for age in ages:
        count[age] += 1

    for a in range(1, 121):
        for b in range(1, 121):
            if a * 0.5 + 7 >= b:
                continue
            if a < b:
                continue
            if a < b * 2:
                total_requests += count[a] * count[b]
                if a == b:
                    total_requests -= count[a]

    return total_requests

## Structure
def numFriendRequests(ages):
    # Your code here

    pass