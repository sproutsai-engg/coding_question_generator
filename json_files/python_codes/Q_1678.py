##Question ID: 1678

def num_ways(s: str) -> int:
    number_of_ones = s.count('1')
    if number_of_ones % 3 != 0:
        return 0

    target = number_of_ones // 3
    if target == 0:
        n = len(s)
        return ((n - 1) * (n - 2) // 2) % 1000000007

    ones_so_far1, ones_so_far2 = 0, 0
    way1, way2 = 0, 0
    for c in s:
        if c == '1':
            ones_so_far1 += 1
            if ones_so_far1 == target:
                way1 += 1
                ones_so_far1 = 0

            ones_so_far2 += 1
            if ones_so_far2 == target * 2:
                way2 += 1
                ones_so_far2 = 0

    return (way1 * way2) % 1000000007


## Structure
def num_ways(s: str) -> int:
    # Your code here

    pass