##Question ID: 1176

def dietPlanPerformance(calories, k, lower, upper):
    points = 0
    T = 0

    for i in range(len(calories)):
        T += calories[i]
        if i >= k:
            T -= calories[i-k]
        if i >= k-1:
            if T < lower: points -= 1
            if T > upper: points += 1

    return points

## Structure
def dietPlanPerformance(calories, k, lower, upper):
    # Your code here

    pass