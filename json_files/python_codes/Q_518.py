##Question ID: 518

def change(amount, coins):
    dp = [1] + [0] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

## Structure
def change(amount, coins):
    # Your code here

    pass