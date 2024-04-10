##Question ID: 353

from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.pos = 0
        self.score = 0
        self.snake = deque([(0, 0)])
        self.occupied = {(0, 0)}
        self.dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
        self.dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

    def move(self, direction: str) -> int:
        new_x = self.snake[-1][0] + self.dx[direction]
        new_y = self.snake[-1][1] + self.dy[direction]

        if new_x < 0 or new_x >= self.height or new_y < 0 or new_y >= self.width:
            return -1

        new_head = (new_x, new_y)
        tail = self.snake.popleft()

        if self.pos < len(self.food) and self.food[self.pos] == list(new_head):
            self.score += 1
            self.pos += 1
        else:
            self.occupied.remove(tail)

        if new_head in self.occupied:
            return -1

        self.snake.append(new_head)
        self.occupied.add(new_head)
        return self.score

## Structure
from collections import deque
    # Your code here

    pass