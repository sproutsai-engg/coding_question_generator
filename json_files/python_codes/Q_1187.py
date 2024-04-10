##Question ID: 1187

from threading import Lock

class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo) -> None:
        for _ in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar) -> None:
        for _ in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()

## Structure
from threading import Lock
    # Your code here

    pass