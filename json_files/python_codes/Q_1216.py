##Question ID: 1216

from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cnt = 1
        self.lock = Lock()

    def zero(self, printNumber):
        for i in range(1, self.n + 1):
            with self.lock:
                while self.cnt % 2 == 0:
                    self.lock.wait()
                printNumber(0)
                self.cnt += 1
                self.lock.notify_all()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            with self.lock:
                while self.cnt != 2 * i:
                    self.lock.wait()
                printNumber(i)
                self.cnt += 1
                self.lock.notify_all()

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            with self.lock:
                while self.cnt != 2 * i - 1:
                    self.lock.wait()
                printNumber(i)
                self.cnt += 1
                self.lock.notify_all()

## Structure
from threading import Lock
    # Your code here

    pass