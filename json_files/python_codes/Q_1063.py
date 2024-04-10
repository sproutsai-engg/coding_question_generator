##Question ID: 1063

def maxScoreSightseeingPair(values):
    max_score = 0
    max_score_left = values[0] + 0
    for j in range(1, len(values)):
        max_score = max(max_score, max_score_left + values[j] - j)
        max_score_left = max(max_score_left, values[j] + j)
    return max_score

## Structure
def maxScoreSightseeingPair(values):
    # Your code here

    pass