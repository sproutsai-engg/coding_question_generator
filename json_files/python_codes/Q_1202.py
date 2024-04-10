##Question ID: 1202

from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)

        # Initialize the parents array
        p = list(range(n))

        # Helper function to find the parent of an index
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        # Union-find, grouping connected indices together
        for pair in pairs:
            root1 = find(pair[0])
            root2 = find(pair[1])
            if root1 != root2:
                p[root2] = root1
                
        # Group all the characters together according to their representatives (parent)
        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(s[i])

        # Sort each group
        for group in groups.values():
            group.sort(reverse=True)

        # Build the result string
        res = []
        for i in range(n):
            root = find(i)
            res.append(groups[root].pop())

        return "".join(res)


## Structure
from collections import defaultdict
    # Your code here

    pass