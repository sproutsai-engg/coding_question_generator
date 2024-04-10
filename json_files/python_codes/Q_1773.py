##Question ID: 1773

def countMatches(items, ruleKey, ruleValue):
    count = 0
    index = {"type": 0, "color": 1, "name": 2}[ruleKey]
    for item in items:
        if item[index] == ruleValue:
            count += 1
    return count

## Structure
def countMatches(items, ruleKey, ruleValue):
    # Your code here

    pass