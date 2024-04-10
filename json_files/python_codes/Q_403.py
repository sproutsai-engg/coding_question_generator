##Question ID: 403

def can_cross(stones):
    dp = {stone: set() for stone in stones}
    dp[0].add(0)

    for stone in stones:
        for k in dp[stone]:
            for jump in (k - 1, k, k + 1):
                if jump > 0 and stone + jump in dp:
                    dp[stone + jump].add(jump)

    return bool(dp[stones[-1]])


## Structure
def can_cross(stones):
    # Your code here

    pass