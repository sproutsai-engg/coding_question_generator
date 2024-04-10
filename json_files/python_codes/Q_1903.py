##Question ID: 1903

def largest_odd_number(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i + 1]
    return ""

## Structure
def largest_odd_number(num: str) -> str:
    # Your code here

    pass