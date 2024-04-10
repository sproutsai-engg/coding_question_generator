##Question ID: 1052

def maxSatisfied(customers, grumpy, minutes):
    total_customers = 0
    max_extra_customers = 0
    extra_customers = 0
    for i in range(len(customers)):
        if grumpy[i] == 0:
            total_customers += customers[i]
        if i < minutes:
            extra_customers += customers[i] * grumpy[i]
        else:
            extra_customers += (customers[i] * grumpy[i]) - (customers[i - minutes] * grumpy[i - minutes])
        max_extra_customers = max(max_extra_customers, extra_customers)
    return total_customers + max_extra_customers


## Structure
def maxSatisfied(customers, grumpy, minutes):
    # Your code here

    pass