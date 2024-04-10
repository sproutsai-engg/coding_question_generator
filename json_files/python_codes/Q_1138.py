##Question ID: 1138

def maxSatisfied(customers, grumpy, minutes):
    total, max_increase, window_increase = 0, 0, 0
    i, j = 0, 0
    while i < len(customers):
        if i - j == minutes:
            window_increase -= customers[j] * grumpy[j]
            j += 1
        window_increase += customers[i] * grumpy[i]
        total += customers[i] * (1 - grumpy[i])
        max_increase = max(max_increase, window_increase)
        i += 1
    return total + max_increase

## Structure
def maxSatisfied(customers, grumpy, minutes):
    # Your code here

    pass