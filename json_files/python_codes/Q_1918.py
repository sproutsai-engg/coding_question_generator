##Question ID: 1918

def maxScore(nums: List[int], k: int) -> int:
    n = len(nums)
    result = 0
    for i in range(k, -1, -1):
        for j in range(k, n):
            min_val = min(nums[i:j+1])
            result = max(result, min_val * (j - i + 1))
    return result

## Structure
def maxScore(nums: List[int], k: int) -> int:
    # Your code here

    pass