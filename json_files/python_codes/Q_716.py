##Question ID: 716

from sortedcontainers import SortedList

class MaxStack:
    def __init__(self):
        self.mainStack = []
        self.maxSet = SortedList()

    def push(self, x: int) -> None:
        self.mainStack.append(x)
        self.maxSet.add(x)

    def pop(self) -> int:
        top = self.mainStack.pop()
        self.maxSet.remove(top)
        return top

    def top(self) -> int:
        return self.mainStack[-1]

    def peekMax(self) -> int:
        return self.maxSet[-1]

    def popMax(self) -> int:
        max_val = self.maxSet.pop()
        tempStack = []
        while self.mainStack[-1] != max_val:
            tempStack.append(self.mainStack.pop())
        self.mainStack.pop()
        while tempStack:
            self.mainStack.append(tempStack.pop())
        return max_val

## Structure
from sortedcontainers import SortedList
    # Your code here

    pass