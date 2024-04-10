##Question ID: 1836

from collections import defaultdict
from typing import List

MOD = 10**9 + 7

def product_ways(queries: List[List[int]]) -> List[int]:
    res = []
    for n, k in queries:
        pf = []
        pm = defaultdict(int)

        i = 2
        while i * i <= k:
            cnt = 0
            while k % i == 0:
                cnt += 1
                k //= i
            if cnt:
                pf.append(cnt)
                pm[cnt] += 1
            i += 1

        if k > 1:
            pm[k] += 1
            pf.append(1)

        ans = 1
        for p in pf:
            ans = (ans * (p * (n - 1) + 1)) % MOD

        res.append(ans)
    return res

## Structure
from collections import defaultdict
    # Your code here

    pass