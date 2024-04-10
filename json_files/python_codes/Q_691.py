##Question ID: 691

from collections import Counter
from functools import lru_cache

def minStickers(stickers, target):
    target_count = Counter(target)
    memo = {}
    
    for s in stickers:
        sticker_count = Counter(s)
        state = ''.join(sticker_count & target_count)
        memo[state] = 1
    
    @lru_cache(None)
    def dp(state):
        counts = Counter(state)
        ans = float('inf')
        for key, value in memo.items():
            if any(counts[ch] < key.count(ch) for ch in state): continue
            ans = min(ans, dp(state.translate(str.maketrans('', '', key))) + value)
        return -1 if ans == float('inf') else ans
    
    return dp(target)

## Structure
from collections import Counter
    # Your code here

    pass