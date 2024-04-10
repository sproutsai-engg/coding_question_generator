##Question ID: 379

from collections import deque

class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.available = [True] * maxNumbers
        self.released = deque()
    
    def get(self) -> int:
        if self.released:
            number = self.released.popleft()
            self.available[number] = False
            return number
        for i in range(len(self.available)):
            if self.available[i]:
                self.available[i] = False
                return i
        return -1
    
    def check(self, number: int) -> bool:
        return self.available[number]
    
    def release(self, number: int) -> None:
        if not self.available[number]:
            self.available[number] = True
            self.released.append(number)


## Structure
from collections import deque
    # Your code here

    pass