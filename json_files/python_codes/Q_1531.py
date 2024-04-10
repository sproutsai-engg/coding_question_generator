##Question ID: 1531

def number_ways(hats):
    kMod = 1000000007
    kMaxHats = 40

    num_people = len(hats)
    people_with_hat = [[] for _ in range(kMaxHats)]

    for i in range(num_people):
        for hat in hats[i]:
            people_with_hat[hat - 1].append(i)

    dp = [[0] * (kMaxHats + 1) for _ in range(1 << num_people)]
    dp[0][0] = 1

    for hat in range(kMaxHats):
        for mask in reversed(range(1 << num_people)):
            dp[mask][hat + 1] = (dp[mask][hat + 1] + dp[mask][hat]) % kMod
            for person in people_with_hat[hat]:
                if mask & (1 << person) == 0:
                    dp[mask | (1 << person)][hat + 1] = (dp[mask | (1 << person)][hat + 1] + dp[mask][hat]) % kMod

    return dp[(1 << num_people) - 1][kMaxHats]

## Structure
def number_ways(hats):
    # Your code here

    pass