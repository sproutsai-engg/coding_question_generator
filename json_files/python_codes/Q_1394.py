##Question ID: 1394

def find_lucky(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    max_lucky = -1
    for num, count in freq.items():
        if num == count:
            max_lucky = max(max_lucky, num)
    return max_lucky

## Structure
def find_lucky(arr):
    # Your code here

    pass