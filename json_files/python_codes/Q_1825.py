##Question ID: 1825

def minimum_working_time(jobs, k):
    max_job = max(jobs)
    sum_jobs = sum(jobs)
    
    left, right = max_job, sum_jobs
    while left < right:
        mid = left + (right - left) // 2
        count, current_sum = 1, 0

        for job in jobs:
            if current_sum + job > mid:
                count += 1
                current_sum = 0
            current_sum += job

        if count <= k:
            right = mid
        else:
            left = mid + 1

    return left


## Structure
def minimum_working_time(jobs, k):
    # Your code here

    pass