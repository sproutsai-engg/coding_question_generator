##Question ID: 1802

from collections import deque

def countStudents(students, sandwiches):
    queue = deque(students)
    index, attempts = 0, 0

    while queue:
        student = queue[0]
        if student == sandwiches[index]:
            queue.popleft()
            index += 1
            attempts = 0
        else:
            queue.rotate(-1)
            attempts += 1

        if attempts == len(queue):
            break

    return len(queue)

## Structure
from collections import deque
    # Your code here

    pass