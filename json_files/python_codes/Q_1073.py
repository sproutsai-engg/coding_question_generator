##Question ID: 1073

from collections import deque

def addNegabinary(arr1, arr2):
    res = deque()
    carry, i, j = 0, len(arr1) - 1, len(arr2) - 1
    while i >= 0 or j >= 0 or carry:
        if i >= 0: carry += arr1[i]; i -= 1
        if j >= 0: carry += arr2[j]; j -= 1
        res.appendleft(carry & 1)
        carry = -(carry >> 1)
    while len(res) > 1 and res[0] == 0: res.popleft()
    return list(res)


## Structure
from collections import deque
    # Your code here

    pass