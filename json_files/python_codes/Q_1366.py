##Question ID: 1366

def rankTeams(votes):
    n, m = len(votes), len(votes[0])
    count = [[0] * m for _ in range(26)]
    res = votes[0]

    for vote in votes:
        for j, team in enumerate(vote):
            count[ord(team) - ord('A')][j] += 1

    return ''.join(sorted(res, key=lambda x: (-count[ord(x) - ord('A')][:m], x)))


## Structure
def rankTeams(votes):
    # Your code here

    pass