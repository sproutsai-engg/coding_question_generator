##Question ID: 1147

from collections import defaultdict

def maxEqualRowsAfterFlips(matrix):
    count = defaultdict(int)
    for row in matrix:
        row_str = "".join(str(row[0] ^ val) for val in row)
        count[row_str] += 1
    return max(count.values())

## Structure
from collections import defaultdict
    # Your code here

    pass