##Question ID: 638

from typing import List

def shoppingOffers(price: List[int], special: List[List[int]], needs: List[int]) -> int:
    def helper(index):
        if index == len(special):
            return sum(needs[i] * price[i] for i in range(len(needs)))

        no_offer = helper(index + 1)
        can_apply_offer = True
        for i in range(len(needs)):
            needs[i] -= special[index][i]
            if needs[i] < 0:
                can_apply_offer = False

        with_offer = float('inf')
        if can_apply_offer:
            offer_cost = special[index][-1] + helper(index)
            with_offer = min(no_offer, offer_cost)

        for i in range(len(needs)):
            needs[i] += special[index][i]
        
        return with_offer if can_apply_offer else no_offer

    return helper(0)


## Structure
from typing import List
    # Your code here

    pass