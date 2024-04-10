##Question ID: 1865

from collections import defaultdict

class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_map = defaultdict(int)
        for num in nums2:
            self.nums2_map[num] += 1

    def add(self, index: int, val: int) -> None:
        self.nums2_map[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2_map[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.nums2_map.get(tot - num, 0) for num in self.nums1)


## Structure
from collections import defaultdict
    # Your code here

    pass