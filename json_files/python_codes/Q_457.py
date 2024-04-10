##Question ID: 457

def circularArrayLoop(nums: List[int]) -> bool:
    N = len(nums)
    for i in range(N):
        slow, fast = i, i
        while True:
            slow = getNextIndex(slow, nums)
            fast = getNextIndex(getNextIndex(fast, nums), nums)
            if slow != fast and nums[slow] * nums[fast] > 0:
                break
            if slow == fast:
                break
        else:
            continue
        cycle = False
        start = slow
        while start != slow:
            cycle |= getNextIndex(start, nums) == start
            start = getNextIndex(start, nums)
        if not cycle:
            return True
    return False

def getNextIndex(idx: int, nums: List[int]) -> int:
    N = len(nums)
    return (idx + nums[idx]) % N


## Structure
def circularArrayLoop(nums: List[int]) -> bool:
    # Your code here

    pass