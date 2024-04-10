##Question ID: 826

def maxProfitAssignment(difficulty, profit, worker):
    n = len(difficulty)
    jobs = sorted(zip(difficulty, profit))
    worker.sort()

    max_profit = 0
    total_profit = 0
    job_idx = 0

    for w in worker:
        while job_idx < n and w >= jobs[job_idx][0]:
            max_profit = max(max_profit, jobs[job_idx][1])
            job_idx += 1
        total_profit += max_profit

    return total_profit

## Structure
def maxProfitAssignment(difficulty, profit, worker):
    # Your code here

    pass