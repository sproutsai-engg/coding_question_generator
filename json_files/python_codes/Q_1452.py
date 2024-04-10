##Question ID: 1452

from typing import List

def peopleIndexes(favoriteCompanies: List[List[str]]) -> List[int]:
    result = []
    companySets = [set(companies) for companies in favoriteCompanies]

    for i, companies in enumerate(companySets):
        isSubset = False
        for j, otherCompanies in enumerate(companySets):
            if i != j and companies.issubset(otherCompanies):
                isSubset = True
                break
        if not isSubset:
            result.append(i)

    return result

## Structure
from typing import List
    # Your code here

    pass