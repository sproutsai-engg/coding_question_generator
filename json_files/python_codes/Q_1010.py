##Question ID: 1010

def powerful_integers(x, y, bound):
    result = set()
    for i in range(20):
        for j in range(20):
            val = x**i + y**j
            if val <= bound:
                result.add(val)
    return list(result)


## Structure
def powerful_integers(x, y, bound):
    # Your code here

    pass