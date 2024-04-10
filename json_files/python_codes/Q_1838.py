##Question ID: 1838

def maxFrequency(nums: List[int], k: int) -> int:
    nums.sort()
    n, i, s, max_freq = len(nums), 0, 0, 0

    for j in range(n):
        s += nums[j]
        while s + k < nums[j] * (j - i + 1):
            s -= nums[i]
            i += 1
        max_freq = max(max_freq, j - i + 1)

    return max_freq

## Structure
def maxFrequency(nums: List[int], k: int) -> int:
    # Your code here

    pass