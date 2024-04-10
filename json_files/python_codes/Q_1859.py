##Question ID: 1859

def min_operations_to_satisfy_conditions(a: str, b: str) -> int:
    same, less, greater = 0, 0, 0

    for i in range(len(a)):
        if a[i] == b[i]:
            same += 1
        elif a[i] < b[i]:
            less += 1
        else:
            greater += 1

    return min(same + max(less, greater), less, greater)

## Structure
def min_operations_to_satisfy_conditions(a: str, b: str) -> int:
    # Your code here

    pass