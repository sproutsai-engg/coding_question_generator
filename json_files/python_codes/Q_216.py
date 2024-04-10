##Question ID: 216

def combinationSum3(k, n):
    def helper(k, n, current, current_comb, result):
        if k == 0 and n == 0:
            result.append(list(current_comb))
        elif k > 0 and n > 0:
            for i in range(current + 1, 10):
                current_comb.append(i)
                helper(k - 1, n - i, i, current_comb, result)
                current_comb.pop()

    result = []
    helper(k, n, 0, [], result)
    return result


## Structure
def combinationSum3(k, n):
    # Your code here

    pass