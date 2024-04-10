##Question ID: 1820

def count_trees(pairs):
    nodes = len(pairs) + 1
    in_degrees = [0] * nodes
    for x, y in pairs:
        in_degrees[y] += 1
    
    res = 1
    for in_degree in in_degrees[1:]:
        res *= in_degree
    
    return res

## Structure
def count_trees(pairs):
    # Your code here

    pass