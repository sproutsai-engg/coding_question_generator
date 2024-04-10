##Question ID: 282

from typing import List

def addOperators(num: str, target: int) -> List[str]:
    def helper(num, target, pos, currVal, prevVal, currExpr):
        if pos == len(num):
            if currVal == target:
                res.append(currExpr)
            return

        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0':
                break

            val = int(num[pos:i + 1])
            if pos == 0:
                helper(num, target, i + 1, val, val, currExpr + num[pos:i + 1])
            else:
                helper(num, target, i + 1, currVal + val, val, currExpr + "+" + num[pos:i + 1])
                helper(num, target, i + 1, currVal - val, -val, currExpr + "-" + num[pos:i + 1])
                helper(num, target, i + 1, currVal - prevVal + prevVal * val, prevVal * val, currExpr + "*" + num[pos:i + 1])

    res = []
    helper(num, target, 0, 0, 0, "")
    return res


## Structure
from typing import List
    # Your code here

    pass