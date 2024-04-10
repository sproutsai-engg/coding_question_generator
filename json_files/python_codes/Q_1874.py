##Question ID: 1874

def can_choose(groups, nums):
    g_i, n_i = 0, 0
    while g_i < len(groups) and n_i + len(groups[g_i]) <= len(nums):
        if nums[n_i : n_i + len(groups[g_i])] == groups[g_i]:
            n_i += len(groups[g_i])
            g_i += 1
        else:
            n_i += 1
    return g_i == len(groups)

## Structure
def can_choose(groups, nums):
    # Your code here

    pass