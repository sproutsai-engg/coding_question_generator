##Question ID: 621

from collections import Counter

def least_interval(tasks, n):
    task_freq = Counter(tasks)

    max_f = max(task_freq.values())
    max_count = sum(1 for count in task_freq.values() if count == max_f)

    return max(len(tasks), (max_f - 1) * (n + 1) + max_count)


## Structure
from collections import Counter
    # Your code here

    pass