##Question ID: 1562

from typing import List

def peopleIndexes(favoriteCompanies: List[List[str]]) -> List[int]:
    result = []
    for i in range(len(favoriteCompanies)):
        is_subset = False
        for j in range(len(favoriteCompanies)):
            if i != j and set(favoriteCompanies[i]).issubset(favoriteCompanies[j]):
                is_subset = True
                break
        if not is_subset:
            result.append(i)
    return result

## Structure
from typing import List
    # Your code here

    pass