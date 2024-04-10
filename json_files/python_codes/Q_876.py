##Question ID: 876

from collections import Counter

def is_n_straight_hand(hand, group_size):
    counts = Counter(hand)

    for card in sorted(counts):
        if counts[card] > 0:
            for i in range(group_size - 1, -1, -1):
                if counts[card + i] < counts[card]:
                    return False
                counts[card + i] -= counts[card]

    return True


## Structure
from collections import Counter
    # Your code here

    pass