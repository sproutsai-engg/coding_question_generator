##Question ID: 414

def third_max(nums):
    top3 = set()
    for num in nums:
        top3.add(num)
        if len(top3) > 3:
            top3.remove(min(top3))
    return min(top3) if len(top3) == 3 else max(top3)

## Structure
def third_max(nums):
    # Your code here

    pass