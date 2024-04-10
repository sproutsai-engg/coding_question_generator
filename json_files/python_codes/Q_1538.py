##Question ID: 1538

def maxScore(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints[:k])

    max_score = total
    for i in range(k - 1, -1, -1):
        j = n - k + i
        total += cardPoints[j] - cardPoints[i]
        max_score = max(max_score, total)

    return max_score


## Structure
def maxScore(cardPoints, k):
    # Your code here

    pass