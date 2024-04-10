##Question ID: 659

def can_split(nums):
    freq = [0] * 20001
    needed = [0] * 20001
    for n in nums:
        freq[n] += 1
    for n in nums:
        if not freq[n]: continue
        if not needed[n - 1]:
            if freq[n + 1] and freq[n + 2]:
                freq[n] -= 1; freq[n + 1] -= 1; freq[n + 2] -= 1;
                needed[n + 2] += 1
            else: return False
        else:
            freq[n] -= 1; needed[n - 1] -= 1;
            needed[n] += 1
    return True

## Structure
def can_split(nums):
    # Your code here

    pass