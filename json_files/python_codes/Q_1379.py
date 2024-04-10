##Question ID: 1379

def reconstructMatrix(upper, lower, colsum):
    result = [[0] * len(colsum) for _ in range(2)]
    
    for i in range(len(colsum)):
        if colsum[i] == 2:
            result[0][i] = 1
            result[1][i] = 1
            upper -= 1
            lower -= 1
        elif colsum[i] == 1:
            if upper > lower:
                result[0][i] = 1
                upper -= 1
            else:
                result[1][i] = 1
                lower -= 1
        
        if upper < 0 or lower < 0:
            return []
    
    if upper > 0 or lower > 0:
        return []
    
    return result

## Structure
def reconstructMatrix(upper, lower, colsum):
    # Your code here

    pass