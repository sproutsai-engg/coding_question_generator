##Question ID: 673

def findNumberOfLIS(nums):
    n = len(nums)
    maxLength = ans = 0
    length = [1] * n
    count = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if length[i] == length[j] + 1:
                    count[i] += count[j]
                elif length[i] < length[j] + 1:
                    length[i] = length[j] + 1
                    count[i] = count[j]
        if maxLength == length[i]:
            ans += count[i]
        elif maxLength < length[i]:
            maxLength = length[i]
            ans = count[i]

    return ans


## Structure
def findNumberOfLIS(nums):
    # Your code here

    pass