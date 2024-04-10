##Question ID: 301

from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        visited = set()
        queue = deque([s])
        result = []
        found = False

        while queue:
            cur = queue.popleft()

            if self.is_valid(cur):
                found = True
                result.append(cur)

            if found: continue

            for i in range(len(cur)):
                if cur[i] == '(' or cur[i] == ')':
                    next_str = cur[:i] + cur[i+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)

        return result

    def is_valid(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == '(': count += 1
            if c == ')':
                count -= 1
                if count < 0: return False
        return count == 0


## Structure
from collections import deque
    # Your code here

    pass