##Question ID: 382

import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        current, result = self.head, 0
        for i, node in enumerate(self.iterate_nodes(current)):
            if random.randint(0, i) == 0:
                result = node.val
        return result

    def iterate_nodes(self, current):
        while current:
            yield current
            current = current.next

## Structure
import random
    # Your code here

    pass