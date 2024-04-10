##Question ID: 1004

def least_ops_express_target(x, target):
    if x == target:
        return 0
    if target == 1:
        return 1
    if x > target:
        return min(2 * target - 1, 2 * (x - target))

    k = 0
    p = x
    while p < target:
        k += 1
        p *= x

    ans = float('inf')
    d = 1

    for i in range(k - 1, -1, -1):
        while p >= target + d * (1 - x):
            p -= d
            ans = min(ans, i + int(math.log2(target // d) + 1) + int(d == 1 and -1 or 0))
        d = d * x + 1

    return ans


## Structure
def least_ops_express_target(x, target):
    # Your code here

    pass