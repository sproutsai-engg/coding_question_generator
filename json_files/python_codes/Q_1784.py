##Question ID: 1784

def minimum_energy(tasks):
    tasks.sort(key=lambda task: task[1] - task[0], reverse=True)

    energy = 0
    for task in tasks:
        energy = max(energy + task[0], task[1])
    return energy

## Structure
def minimum_energy(tasks):
    # Your code here

    pass