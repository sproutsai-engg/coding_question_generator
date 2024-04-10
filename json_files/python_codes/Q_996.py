##Question ID: 996

from collections import Counter

def numSquarefulPerms(nums):
    def is_square(n):
        return int(n ** 0.5) ** 2 == n

    def dfs(idx):
        if idx == len(nums):
            return 1

        count = 0
        for key in counter.keys():
            if counter[key] and (idx == 0 or is_square(nums[idx - 1] + key)):
                counter[key] -= 1
                nums[idx] = key
                count += dfs(idx + 1)
                counter[key] += 1

        return count

    key_set, counter = set(nums), Counter(nums)
    return dfs(0)


## Structure
from collections import Counter
    # Your code here

    pass