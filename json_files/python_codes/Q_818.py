##Question ID: 818

def racecar(target: int) -> int:
    memo = {}
    def dp(position, speed):
        if abs(position) > 2 * target:
            return target + 1
        if position == target:
            return 0 if speed == 1 else 1
        if (position, speed) in memo:
            return memo[(position, speed)]
        
        ans = dp(position + speed // 2, -speed // 2) + 1 if speed > 0 else dp(position - speed // 2, -speed // 2) + 1
        ans = min(ans, dp(position + speed, speed * 2) + 1)
        memo[(position, speed)] = ans
        return ans
    
    return dp(0, 1)

## Structure
def racecar(target: int) -> int:
    # Your code here

    pass