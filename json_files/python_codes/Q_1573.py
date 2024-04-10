##Question ID: 1573

def min_sum_of_lengths(arr, target):
    n = len(arr)
    sum_, min_len, result = 0, float('inf'), float('inf')
    mp = {0: -1}

    for i in range(n):
        sum_ += arr[i]
        if sum_ >= target and (sum_ - target) in mp:
            if mp[sum_ - target] > -1 and min_len != float('inf'):
                result = min(result, i - mp[sum_ - target] + min_len)
            min_len = min(min_len, i - mp[sum_ - target])
        mp[sum_] = i

    return result if result != float('inf') else -1


## Structure
def min_sum_of_lengths(arr, target):
    # Your code here

    pass