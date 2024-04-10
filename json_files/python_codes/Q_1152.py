##Question ID: 1152

from typing import List
from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        visits = defaultdict(list)
        
        # user_visits: {user: [(timestamp, website),...]}
        for i in range(n):
            visits[username[i]].append((timestamp[i], website[i]))


        for user in visits:
            visits[user].sort()
        
        patterns = defaultdict(int)
        
        for user in visits:
            websites = [web for _, web in visits[user]]
            patterns_set = set(combinations(websites, 3))

            for pattern in patterns_set:
                patterns[pattern] += 1
                
        patterns = sorted(patterns.items(), key=lambda x: (-x[1], x[0]))
        
        return list(patterns[0][0])


## Structure
from typing import List
    # Your code here

    pass