##Question ID: 1817

def total_money(n):
    weeks = n // 7
    days_remaining = n % 7
    return 28 * weeks + 7 * weeks * (weeks - 1) // 2 + (weeks + 1) * days_remaining + days_remaining * (days_remaining - 1) // 2


## Structure
def total_money(n):
    # Your code here

    pass