##Question ID: 1503

def max_satisfaction(satisfaction):
    satisfaction.sort(reverse=True)
    ans = total = sum = 0
    for i in satisfaction:
        total += i
        if total > 0:
            sum += total
            ans = max(ans, sum)
    return ans

## Structure
def max_satisfaction(satisfaction):
    # Your code here

    pass