##Question ID: 1203

from threading import Condition

class Foo:
    def __init__(self):
        self.order = 1
        self.cv = Condition()

    def first(self):
        with self.cv:
            # printFirst() outputs "first". Do not change or remove this line.
            printFirst()
            self.order = 2
            self.cv.notify_all()

    def second(self):
        with self.cv:
            self.cv.wait_for(lambda: self.order == 2)
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.order = 3
            self.cv.notify_all()

    def third(self):
        with self.cv:
            self.cv.wait_for(lambda: self.order == 3)
            # printThird() outputs "third". Do not change or remove this line.
            printThird()

## Structure
from threading import Condition
    # Your code here

    pass