##Question ID: 1055

def num_pairs_divisible_by60(time):
    count = [0] * 60
    pairs = 0

    for t in time:
        mod = t % 60
        pairs += count[(60 - mod) % 60]
        count[mod] += 1

    return pairs

## Structure
def num_pairs_divisible_by60(time):
    # Your code here

    pass