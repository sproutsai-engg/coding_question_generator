##Question ID: 853

def max_profit_assignment(difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit))
    worker.sort()

    i, max_profit, total_profit = 0, 0, 0
    for ability in worker:
        while i < len(difficulty) and ability >= jobs[i][0]:
            max_profit = max(max_profit, jobs[i][1])
            i += 1
        total_profit += max_profit
    return total_profit

## Structure
def max_profit_assignment(difficulty, profit, worker):
    # Your code here

    pass