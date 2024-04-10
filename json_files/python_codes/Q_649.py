##Question ID: 649

from collections import deque

def predict_party_victory(senate: str) -> str:
    radiant = deque()
    dire = deque()
    n = len(senate)
    
    for i, s in enumerate(senate):
        if s == 'R':
            radiant.append(i)
        else:
            dire.append(i)

    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()

        if r < d:
            radiant.append(r + n)
        else:
            dire.append(d + n)

    return "Dire" if not radiant else "Radiant"


## Structure
from collections import deque
    # Your code here

    pass