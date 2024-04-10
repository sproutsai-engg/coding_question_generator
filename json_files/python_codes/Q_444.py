##Question ID: 444

def is_shortest_and_unique_supersequence(nums, sequences):
    pos = {val: idx for idx, val in enumerate(nums)}

    for seq in sequences:
        if pos[seq[0]] > pos[seq[-1]]:
            return False
    return True

## Structure
def is_shortest_and_unique_supersequence(nums, sequences):
    # Your code here

    pass