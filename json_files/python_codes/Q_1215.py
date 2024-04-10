##Question ID: 1215

def countSteppingNumbers(low, high):
    results = []
    for i in range(low, high+1):
        prev = -1
        j = i
        is_stepping = True
        while j > 0:
            digit = j % 10
            if prev != -1 and abs(prev - digit) != 1:
                is_stepping = False
                break
            prev = digit
            j //= 10
        if is_stepping:
            results.append(i)
    return results

## Structure
def countSteppingNumbers(low, high):
    # Your code here

    pass