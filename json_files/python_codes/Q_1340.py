##Question ID: 1340

import threading

class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]
        self.not_busy = [threading.Condition(self.forks[i]) for i in range(5)]

    def wantsToEat(self, philosopher: int, pickLeftFork: 'Callable[[], None]', pickRightFork: 'Callable[[], None]', eat: 'Callable[[], None]', putLeftFork: 'Callable[[], None]', putRightFork: 'Callable[[], None]') -> None:
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5

        with self.forks[left_fork]:
            with self.not_busy[left_fork]:
                while not self.forks[right_fork].acquire(blocking=False):
                    self.not_busy[left_fork].wait()
            pickLeftFork()

            with self.forks[right_fork]:
                pickRightFork()
                eat()
                putRightFork()
                self.forks[right_fork].release()
                with self.not_busy[right_fork]:
                    self.not_busy[right_fork].notify_all()

            putLeftFork()
            self.not_busy[left_fork].notify_all()

## Structure
import threading
    # Your code here

    pass