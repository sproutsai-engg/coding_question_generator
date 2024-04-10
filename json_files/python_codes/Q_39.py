##Question ID: 39

def combinationSum(candidates, target):
    def findCombinations(startIndex, remaining):
        if remaining == 0:
            return [[]]
        if startIndex == len(candidates) or remaining < 0:
            return []

        result = []
        result.extend(findCombinations(startIndex + 1, remaining))
        result.extend([x + [candidates[startIndex]] for x in findCombinations(startIndex, remaining - candidates[startIndex])])
        
        return result

    return findCombinations(0, target)


## Structure
def combinationSum(candidates, target):
    # Your code here

    pass