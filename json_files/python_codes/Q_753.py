##Question ID: 753

from collections import deque

def openLock(deadends, target):
    dead = set(deadends)
    visited = set()
    wheel_states = deque([("0000", 0)])

    if "0000" in dead:
        return -1

    while wheel_states:
        current_state, turns = wheel_states.popleft()

        if current_state == target:
            return turns

        for i in range(4):
            up_state = current_state[:i] + str((int(current_state[i]) + 1) % 10) + current_state[i + 1:]
            down_state = current_state[:i] + str((int(current_state[i]) - 1) % 10) + current_state[i + 1:]

            if up_state not in visited and up_state not in dead:
                wheel_states.append((up_state, turns + 1))
                visited.add(up_state)

            if down_state not in visited and down_state not in dead:
                wheel_states.append((down_state, turns + 1))
                visited.add(down_state)

    return -1

## Structure
from collections import deque
    # Your code here

    pass