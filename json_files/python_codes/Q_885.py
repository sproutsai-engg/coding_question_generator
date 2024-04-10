##Question ID: 885

from bisect import bisect_left, insort_left

class ExamRoom:

    def __init__(self, n: int):
        self.students = []
        self.n = n

    def seat(self) -> int:
        if not self.students:
            seat_index = 0
        else:
            distance, seat_index = self.students[0], 0
            
            for i in range(1, len(self.students)):
                d = (self.students[i] - self.students[i - 1]) // 2
                if d > distance:
                    distance = d
                    seat_index = self.students[i - 1] + d
                    
            if self.n - 1 - self.students[-1] > distance:
                seat_index = self.n - 1
                
        insort_left(self.students, seat_index)
        return seat_index

    def leave(self, p: int) -> None:
        index = bisect_left(self.students, p)
        self.students.pop(index)


## Structure
from bisect import bisect_left, insort_left
    # Your code here

    pass