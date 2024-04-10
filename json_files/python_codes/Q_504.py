##Question ID: 504

def convert_to_base7(num: int) -> str:
    if num == 0:
        return "0"
    result = ""
    negative = num < 0
    if negative:
        num *= -1
    while num > 0:
        result = str(num % 7) + result
        num //= 7
    return "-" + result if negative else result

## Structure
def convert_to_base7(num: int) -> str:
    # Your code here

    pass