##Question ID: 1812

def reformat_number(number):
    cleaned_number = ''.join(c for c in number if c.isdigit())

    blocks = []
    n = len(cleaned_number)
    i = 0
    while i < n:
        if n - i == 2 or n - i == 4:
            blocks.append(cleaned_number[i:i + 2])
            i += 2
        else:
            blocks.append(cleaned_number[i:i + 3])
            i += 3

    return '-'.join(blocks)

## Structure
def reformat_number(number):
    # Your code here

    pass