##Question ID: 1186

from threading import Semaphore

class H2O:
    def __init__(self):
        self.hydrogenSemaphore = Semaphore(2)
        self.oxygenSemaphore = Semaphore(1)

    def hydrogen(self, releaseHydrogen):
        self.hydrogenSemaphore.acquire()
        releaseHydrogen()
        self.oxygenSemaphore.release()

    def oxygen(self, releaseOxygen):
        self.oxygenSemaphore.acquire()
        releaseOxygen()
        self.hydrogenSemaphore.release(2)

## Structure
from threading import Semaphore
    # Your code here

    pass