##Question ID: 1074

def numSubmatrixSumTarget(matrix: List[List[int]], target: int) -> int:
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows):
        for col in range(1, cols):
            matrix[row][col] += matrix[row][col-1]
    
    count = 0
    for col1 in range(cols):
        for col2 in range(col1, cols):
            counter = collections.defaultdict(int)
            counter[0] = 1
            cur_sum = 0
            for row in range(rows):
                cur_sum += matrix[row][col2] - (matrix[row][col1-1] if col1 > 0 else 0)
                count += counter[cur_sum - target]
                counter[cur_sum] += 1

    return count

## Structure
def numSubmatrixSumTarget(matrix: List[List[int]], target: int) -> int:
    # Your code here

    pass