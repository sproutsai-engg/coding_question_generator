##Question ID: 440

def find_kth_number(n, k):
    nums = [i for i in range(1, n + 1)]
    nums.sort(key=lambda x: str(x))
    return nums[k - 1]


## Structure
def find_kth_number(n, k):
    # Your code here

    pass