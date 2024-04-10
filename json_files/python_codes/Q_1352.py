##Question ID: 1352

from functools import lru_cache

class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

def find_next_job(jobs, i):
    for j in range(i + 1, len(jobs)):
        if jobs[j].start >= jobs[i].end:
            return j
    return -1

@lru_cache(None)
def max_profit_helper(jobs, i):
    if i == -1:
        return 0

    next_job = find_next_job(jobs, i)
    incl_curr_job = jobs[i].profit + max_profit_helper(jobs, next_job)
    excl_curr_job = max_profit_helper(jobs, i - 1)
    
    return max(incl_curr_job, excl_curr_job)

def max_profit(startTime, endTime, profit):
    n = len(startTime)
    jobs = [Job(startTime[i], endTime[i], profit[i]) for i in range(n)]

    jobs.sort(key=lambda job: job.end)
    
    return max_profit_helper(tuple(jobs), n - 1)

## Structure
from functools import lru_cache
    # Your code here

    pass