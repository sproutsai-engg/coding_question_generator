##Question ID: 1262

from collections import defaultdict
from random import randint

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.positions = defaultdict(list)
        for i, num in enumerate(arr):
            self.positions[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            randomIndex = randint(left, right)
            num = self.arr[randomIndex]
            lb = self.lower_bound(self.positions[num], left)
            ub = self.upper_bound(self.positions[num], right)
            if ub - lb >= threshold:
                return num
        return -1

    def lower_bound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

    def upper_bound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l

## Structure
from collections import defaultdict
    # Your code here

    pass