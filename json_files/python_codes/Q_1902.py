##Question ID: 1902

def get_collision_times(cars):
    n = len(cars)
    collisions = [-1] * n
    for i in range(n-1, -1, -1):
        time_to_collision = 1e9
        for j in range(i+1, n):
            if cars[j][1] > cars[i][1]:
                continue
            current_collision = (cars[j][0] - cars[i][0]) / (cars[i][1] - cars[j][1])
            if current_collision < time_to_collision:
                time_to_collision = min(time_to_collision, min(collisions[j], current_collision))
        collisions[i] = -1.0 if time_to_collision == 1e9 else time_to_collision
    return collisions

## Structure
def get_collision_times(cars):
    # Your code here

    pass