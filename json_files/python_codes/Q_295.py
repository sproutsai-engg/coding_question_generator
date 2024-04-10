##Question ID: 295

import heapq

class MedianFinder:
    def __init__(self):
        self.left = []  # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        elif len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]


## Structure
import heapq
    # Your code here

    pass