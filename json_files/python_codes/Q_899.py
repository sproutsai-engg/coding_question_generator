##Question ID: 899

def longest_distance(n):
    last = -1
    longest = 0
    i = 0
    while n:
        if n & 1:
            if last >= 0:
                longest = max(longest, i - last)
            last = i
        n >>= 1
        i += 1
    return longest

## Structure
def longest_distance(n):
    # Your code here

    pass