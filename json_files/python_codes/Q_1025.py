##Question ID: 1025

def mincostTickets(days, costs):
  travel_days = set(days)
  dp = [0] * 366

  for i in range(1, 366):
    if i not in travel_days:
      dp[i] = dp[i - 1]
    else:
      dp[i] = min(dp[i - 1] + costs[0],
                  dp[max(0, i - 7)] + costs[1],
                  dp[max(0, i - 30)] + costs[2])

  return dp[365]

## Structure
def mincostTickets(days, costs):
    # Your code here

    pass