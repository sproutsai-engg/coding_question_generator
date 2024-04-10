##Question ID: 363

from sortedcontainers import SortedList

def maxSumSubmatrix(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    for l in range(cols):
        sums = [0] * rows
        for r in range(l, cols):
            for i in range(rows):
                sums[i] += matrix[i][r]

            sorted_sums = SortedList()
            sorted_sums.add(0)
            curr_sum = 0
            for sum in sums:
                curr_sum += sum
                it = sorted_sums.bisect_left(curr_sum - k)
                if it != len(sorted_sums):
                    max_sum = max(max_sum, curr_sum - sorted_sums[it])
                sorted_sums.add(curr_sum)

    return max_sum


## Structure
from sortedcontainers import SortedList
    # Your code here

    pass