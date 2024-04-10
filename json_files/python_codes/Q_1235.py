##Question ID: 1235

from bisect import bisect_left

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(endTime, startTime, profit))
    dp = [jobs[0][2]]
    
    def latestNonConflict(index):
        startTimeToFind = jobs[index][1]
        index = bisect_left([job[0] for job in jobs], startTimeToFind)
        if index:
            return index - 1
        return -1

    for i in range(1, len(jobs)):
        L = latestNonConflict(i)
        dp.append(max(dp[-1], (0 if L == -1 else dp[L]) + jobs[i][2]))

    return dp[-1]

## Structure
from bisect import bisect_left
    # Your code here

    pass