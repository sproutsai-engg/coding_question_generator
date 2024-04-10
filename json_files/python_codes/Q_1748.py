##Question ID: 1748

def bestTeamScore(scores, ages):
    players = sorted(zip(ages, scores))
    n = len(players)
    dp = [0] * n
    best_score = 0
    
    for i in range(n):
        dp[i] = players[i][1]
        for j in range(i):
            if players[i][1] >= players[j][1]:
                dp[i] = max(dp[i], dp[j] + players[i][1])
        best_score = max(best_score, dp[i])
    
    return best_score


## Structure
def bestTeamScore(scores, ages):
    # Your code here

    pass