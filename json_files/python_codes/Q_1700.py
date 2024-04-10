##Question ID: 1700

def min_time_to_remove_balloons(colors, neededTime):
    n = len(colors)
    INF = 10**9
    dp = [[INF] * 26 for _ in range(n)]

    for color in range(26):
        if colors[0] != chr(ord('A') + color):
            dp[0][color] = neededTime[0]

    for i in range(1, n):
        for color1 in range(26):
            for color2 in range(26):
                if color1 != color2 and colors[i] != chr(ord('A') + color1):
                    dp[i][color1] = min(dp[i][color1], dp[i-1][color2] + neededTime[i])

    ans = INF
    for color in range(26):
        ans = min(ans, dp[n-1][color])

    return ans


## Structure
def min_time_to_remove_balloons(colors, neededTime):
    # Your code here

    pass