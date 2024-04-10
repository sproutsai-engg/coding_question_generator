##Question ID: 1830

from collections import defaultdict

def countPairs(deliciousness):
    MOD = 10**9 + 7
    hashMap = defaultdict(int)
    maxVal = max(deliciousness)
    maxSum = maxVal * 2

    count = 0
    for val in deliciousness:
        for sum in (1 << i for i in range(22)):
            count = (count + hashMap[sum - val]) % MOD
        hashMap[val] += 1

    return count

## Structure
from collections import defaultdict
    # Your code here

    pass