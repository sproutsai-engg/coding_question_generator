##Question ID: 814

def best_rotation(nums):
    n = len(nums)
    change = [0] * n

    for i in range(n):
        change[(i - nums[i] + 1 + n) % n] -= 1
        change[(i + 1) % n] += 1

    max_score = 0
    cur_score = change[0]
    for i in range(1, n):
        cur_score += change[i]
        if cur_score > max_score:
            max_score = cur_score
            
    return max_score


## Structure
def best_rotation(nums):
    # Your code here

    pass