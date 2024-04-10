##Question ID: 1500

def countLargestGroup(n: int) -> int:
    freq = [0] * 37
    max_group_size = 0
    max_group_count = 0
    
    for i in range(1, n + 1):
        _sum = sum(map(int, str(i)))
        freq[_sum] += 1
        max_group_size = max(max_group_size, freq[_sum])
    
    for count in freq:
        if count == max_group_size:
            max_group_count += 1

    return max_group_count


## Structure
def countLargestGroup(n: int) -> int:
    # Your code here

    pass