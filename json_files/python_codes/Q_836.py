##Question ID: 836

def racecar(target: int) -> int:
    memo = {}

    def dp(pos: int, speed: int) -> int:
        if pos == target:
            return 0
        if abs(pos) > 2 * target:
            return float('inf')

        key = (pos, speed)
        if key in memo:
            return memo[key]

        op1 = dp(pos + speed, speed * 2) + 1
        op2 = dp(pos, -speed) + 2

        ans = min(op1, op2)
        memo[key] = ans
        return ans

    return dp(0, 1)

## Structure
def racecar(target: int) -> int:
    # Your code here

    pass