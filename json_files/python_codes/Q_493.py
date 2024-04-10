##Question ID: 493

def reversePairs(nums):
    def mergeSort(l, r):
        if l >= r:
            return 0
        
        mid = (l + r) // 2
        count = mergeSort(l, mid) + mergeSort(mid + 1, r)
        j = mid + 1
        for i in range(l, mid + 1):
            while j <= r and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)
        
        nums[l:r + 1] = sorted(nums[l:r + 1])
        
        return count
    
    return mergeSort(0, len(nums) - 1)


## Structure
def reversePairs(nums):
    # Your code here

    pass