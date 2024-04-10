##Question ID: 726

from collections import Counter

def parse(formula, i):
    counts = Counter()
    while i[0] < len(formula):
        if formula[i[0]] == '(':
            i[0] += 1
            temp = parse(formula, i)
            count = 0
            while i[0] < len(formula) and formula[i[0]].isdigit():
                count = count * 10 + int(formula[i[0]])
                i[0] += 1
            if count == 0: count = 1
            for name, c in temp.items():
                counts[name] += c * count
        elif formula[i[0]] == ')':
            i[0] += 1
            return counts
        else:
            name = formula[i[0]]
            i[0] += 1
            while i[0] < len(formula) and formula[i[0]].islower():
                name += formula[i[0]]
                i[0] += 1
            count = 0
            while i[0] < len(formula) and formula[i[0]].isdigit():
                count = count * 10 + int(formula[i[0]])
                i[0] += 1
            if count == 0: count = 1
            counts[name] += count
    return counts

def countOfAtoms(formula):
    i = [0]
    counts = parse(formula, i)
    ans = []
    for name, count in counts.items():
        ans.append(name)
        if count > 1: ans.append(str(count))
    return ''.join(ans)


## Structure
from collections import Counter
    # Your code here

    pass