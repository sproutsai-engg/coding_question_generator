##Question ID: 940

def totalFruit(fruits):
    left, right, max_count = 0, 0, 0
    count = {}

    while right < len(fruits):
        count[fruits[right]] = count.get(fruits[right], 0) + 1
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1
        max_count = max(max_count, right - left + 1)
        right += 1

    return max_count

## Structure
def totalFruit(fruits):
    # Your code here

    pass