##Question ID: 1399

def countLargestGroup(n: int) -> int:
    groups = [0] * 37
    largest_group_size = 0
    count_largest_groups = 0

    for i in range(1, n + 1):
        sum_of_digits = sum(map(int, str(i)))
        groups[sum_of_digits] += 1
        if groups[sum_of_digits] > largest_group_size:
            largest_group_size = groups[sum_of_digits]
            count_largest_groups = 1
        elif groups[sum_of_digits] == largest_group_size:
            count_largest_groups += 1

    return count_largest_groups

## Structure
def countLargestGroup(n: int) -> int:
    # Your code here

    pass