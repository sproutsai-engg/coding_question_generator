##Question ID: 171

def title_to_number(column_title: str) -> int:
    result = 0
    for c in column_title:
        result = result * 26 + (ord(c) - ord('A') + 1)
    return result

## Structure
def title_to_number(column_title: str) -> int:
    # Your code here

    pass