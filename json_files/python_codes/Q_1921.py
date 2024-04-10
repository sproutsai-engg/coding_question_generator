##Question ID: 1921

def eliminate_maximum(dist, speed):
    n = len(dist)
    time_to_reach_city = [(dist[i] + speed[i] - 1) // speed[i] for i in range(n)]
    time_to_reach_city.sort()
    eliminated = 0
    for i in range(n):
        if time_to_reach_city[i] > i:
            eliminated += 1
        else:
            break
    return eliminated

## Structure
def eliminate_maximum(dist, speed):
    # Your code here

    pass