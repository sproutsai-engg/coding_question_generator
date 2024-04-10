##Question ID: 646

def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1])

    max_chain_length = 0
    last_right = float('-inf')
    for pair in pairs:
        if pair[0] > last_right:
            last_right = pair[1]
            max_chain_length += 1

    return max_chain_length


## Structure
def findLongestChain(pairs):
    # Your code here

    pass