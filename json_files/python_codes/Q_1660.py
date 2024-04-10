##Question ID: 1660

def thousand_separator(n: int) -> str:
    result = str(n)
    count = 0
    for i in range(len(result) - 1, 0, -1):
        count += 1
        if count % 3 == 0:
            result = result[:i] + '.' + result[i:]
    return result

## Structure
def thousand_separator(n: int) -> str:
    # Your code here

    pass