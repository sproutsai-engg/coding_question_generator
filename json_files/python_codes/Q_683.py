##Question ID: 683

def kEmptySlots(bulbs, k):
    days = [0] * len(bulbs)
    for i, bulb in enumerate(bulbs):
        days[bulb - 1] = i

    ans = float('inf')
    left = 0
    right = k + 1
    while right < len(days):
        i = left + 1
        for i in range(left + 1, right):
            if days[i] < days[left] or days[i] < days[right]:
                left = i
                break
        else:
            ans = min(ans, max(days[left], days[right]))
            left += 1
            right += 1

    return -1 if ans == float('inf') else ans + 1


## Structure
def kEmptySlots(bulbs, k):
    # Your code here

    pass