##Question ID: 1665

def minimumEffort(tasks):
    tasks.sort(key=lambda task: task[1] - task[0], reverse=True)
    ans, sum_energy = 0, 0
    for task in tasks:
        ans = max(ans, sum_energy + task[1])
        sum_energy += task[0]
    return ans

## Structure
def minimumEffort(tasks):
    # Your code here

    pass