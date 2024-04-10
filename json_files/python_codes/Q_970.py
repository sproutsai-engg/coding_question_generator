##Question ID: 970

def powerfulIntegers(x, y, bound):
    max_i = 0 if x == 1 else int(math.log(bound, x))
    max_j = 0 if y == 1 else int(math.log(bound, y))
    result_set = set()
    
    for i in range(max_i + 1):
        for j in range(max_j + 1):
            powerful_num = x ** i + y ** j
            if powerful_num <= bound:
                result_set.add(powerful_num)
                
    return list(result_set)

## Structure
def powerfulIntegers(x, y, bound):
    # Your code here

    pass