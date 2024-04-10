##Question ID: 1839

def decode(encoded, first):
    arr = [first]
    for num in encoded:
        arr.append(arr[-1] ^ num)
    return arr


## Structure
def decode(encoded, first):
    # Your code here

    pass