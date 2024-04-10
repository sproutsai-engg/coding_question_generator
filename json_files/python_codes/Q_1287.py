##Question ID: 1287

def shortest_distance(distance, start, destination):
    total_distance = sum(distance)
    clockwise_distance = sum(distance[start:destination])
    
    return min(clockwise_distance, total_distance - clockwise_distance)

## Structure
def shortest_distance(distance, start, destination):
    # Your code here

    pass