##Question ID: 842

def smallest_good_integer(fronts, backs):
    not_good = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}

    result = float('inf')
    for i in range(len(fronts)):
        if fronts[i] not in not_good:
            result = min(result, fronts[i])
        if backs[i] not in not_good:
            result = min(result, backs[i])

    return 0 if result == float('inf') else result

## Structure
def smallest_good_integer(fronts, backs):
    # Your code here

    pass