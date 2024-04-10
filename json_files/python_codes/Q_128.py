##Question ID: 128

def longest_consecutive(nums):
    elements = set(nums)
    longest_seq = 0

    for num in nums:
        if num - 1 not in elements:
            current_num = num
            current_seq = 1
            
            while current_num + 1 in elements:
                current_num += 1
                current_seq += 1

            longest_seq = max(longest_seq, current_seq)
    
    return longest_seq

## Structure
def longest_consecutive(nums):
    # Your code here

    pass