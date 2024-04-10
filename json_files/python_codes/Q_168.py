##Question ID: 168

def convert_to_title(columnNumber: int) -> str:
    result = ""
    while columnNumber:
        columnNumber -= 1
        result = chr(columnNumber % 26 + ord('A')) + result
        columnNumber //= 26
    return result


## Structure
def convert_to_title(columnNumber: int) -> str:
    # Your code here

    pass