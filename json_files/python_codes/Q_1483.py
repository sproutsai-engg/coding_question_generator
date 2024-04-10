##Question ID: 1483

def rank_teams(votes):
    teams = len(votes[0])
    ranks = [[0] * teams for _ in range(26)]

    for vote in votes:
        for i in range(teams):
            ranks[ord(vote[i]) - ord('A')][i] += 1

    result = list(votes[0])
    result.sort(key=lambda ch: tuple([-ranks[ord(ch) - ord('A')][i] for i in range(teams)] + [ch]))
    return ''.join(result)


## Structure
def rank_teams(votes):
    # Your code here

    pass