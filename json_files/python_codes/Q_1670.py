##Question ID: 1670

from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.first = deque()
        self.second = deque()

    def pushFront(self, val: int) -> None:
        self.first.appendleft(val)
        if len(self.first) > len(self.second) + 1:
            self.second.appendleft(self.first.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.first) < len(self.second):
            self.first.append(val)
        else:
            self.second.appendleft(val)

    def pushBack(self, val: int) -> None:
        self.second.append(val)
        if len(self.second) > len(self.first):
            self.first.append(self.second.popleft())

    def popFront(self) -> int:
        if not self.first and not self.second:
            return -1
        val = self.first.popleft()
        if len(self.first) + 1 < len(self.second):
            self.first.append(self.second.popleft())
        return val

    def popMiddle(self) -> int:
        if not self.first and not self.second:
            return -1
        if len(self.first) < len(self.second):
            val = self.second.popleft()
        else:
            val = self.first.pop()
        if len(self.second) > len(self.first):
            self.first.append(self.second.popleft())
        return val

    def popBack(self) -> int:
        if not self.first and not self.second:
            return -1
        val = self.second.pop()
        if len(self.first) > len(self.second) + 1:
            self.second.appendleft(self.first.pop())
        return val


## Structure
from collections import deque
    # Your code here

    pass