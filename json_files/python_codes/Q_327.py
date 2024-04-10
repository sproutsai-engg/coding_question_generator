##Question ID: 327

def countRangeSum(nums, lower, upper):
    sums = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        sums[i + 1] = sums[i] + nums[i]

    def mergeSort(start, end):
        if start == end:
            return 0
        mid = start + (end - start) // 2
        count = mergeSort(start, mid) + mergeSort(mid + 1, end)

        j, k = mid + 1, mid + 1
        for i in range(start, mid + 1):
            while j <= end and sums[j] - sums[i] < lower: j += 1
            while k <= end and sums[k] - sums[i] <= upper: k += 1
            count += k - j

        sums[start:end + 1] = sorted(sums[start:end + 1])
        return count

    return mergeSort(0, len(nums))

## Structure
def countRangeSum(nums, lower, upper):
    # Your code here

    pass