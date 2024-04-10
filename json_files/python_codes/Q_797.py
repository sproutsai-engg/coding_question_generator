##Question ID: 797

from collections import defaultdict
def numRabbits(answers):
    count = defaultdict(int)
    res = 0
    for a in answers:
        count[a] += 1
        if count[a] == 1:
            res += (a + 1)
        elif count[a] > a + 1:
            count[a] = 1
            res += (a + 1)
    return res


## Structure
from collections import defaultdict
    # Your code here

    pass