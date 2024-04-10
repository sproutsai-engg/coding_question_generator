##Question ID: 1525

def process_queries(queries, m):
    nums = list(range(1, m+1))
    result = []
    for q in queries:
        pos = nums.index(q)
        result.append(pos)
        del nums[pos]
        nums.insert(0, q)
    return result

## Structure
def process_queries(queries, m):
    # Your code here

    pass