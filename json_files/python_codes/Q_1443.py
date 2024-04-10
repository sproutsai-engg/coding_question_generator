##Question ID: 1443

def minimum_distance(word: str) -> int:
    def dp(first: int, second: int, pos: int) -> int:
        if pos == len(word): return 0
        
        ans = float('inf')
        for i in [first, second]:
            if i != -1:
                dx = abs(ord(word[pos]) - ord(word[i])) % 6
                dy = abs(ord(word[pos]) - ord(word[i])) // 6
                ans = min(ans, min(dx, dy) * 2 + max(dx, dy))
        ans += dp(first, second, pos + 1)

        if first == -1 or second == -1:
            ans = min(ans, dp(pos if first == -1 else first, ord(word[pos]), pos + 1))

        return ans
    
    return dp(-1, -1, 0)


## Structure
def minimum_distance(word: str) -> int:
    # Your code here

    pass