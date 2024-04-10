##Question ID: 846

from collections import Counter

def is_possible_divide(hand, group_size):
    card_count = Counter(hand)

    for card in sorted(card_count):
        if card_count[card] > 0:
            count = card_count[card]
            for i in range(1, group_size):
                if card_count[card + i] < count:
                    return False
                card_count[card + i] -= count

    return True


## Structure
from collections import Counter
    # Your code here

    pass