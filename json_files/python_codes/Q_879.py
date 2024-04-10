##Question ID: 879

def max_dist_to_closest(seats):
    max_dist = 0
    last_person = -1
    for i, seat in enumerate(seats):
        if seat == 1:
            max_dist = i if last_person < 0 else max(max_dist, (i - last_person) // 2)
            last_person = i
    return max(max_dist, len(seats) - 1 - last_person)

## Structure
def max_dist_to_closest(seats):
    # Your code here

    pass