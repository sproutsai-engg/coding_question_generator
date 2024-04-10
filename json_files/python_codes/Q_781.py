##Question ID: 781

from collections import Counter

def numRabbits(answers):
    count = Counter(answers)
    rabbits = 0
    for ans, cnt in count.items():
        rabbits += (ans + cnt)//(ans + 1) * (ans + 1)
    return rabbits


## Structure
from collections import Counter
    # Your code here

    pass