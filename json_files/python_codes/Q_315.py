##Question ID: 315

def countSmaller(nums):
    def merge_sort(indices):
        if len(indices) <= 1:
            return indices
        mid = len(indices) // 2
        left = merge_sort(indices[:mid])
        right = merge_sort(indices[mid:])
        return merge(left, right)

    def merge(left, right):
        merged, count = [], 0
        while left and right:
            if nums[left[0]] <= nums[right[0]]:
                counts[left[0]] += count
                merged.append(left.pop(0))
            else:
                count += len(left)
                merged.append(right.pop(0))
        for i in left:
            counts[i] += count
        return merged + left + right

    counts = [0] * len(nums)
    merge_sort(list(range(len(nums))))
    return counts

## Structure
def countSmaller(nums):
    # Your code here

    pass