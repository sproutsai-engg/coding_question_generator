##Question ID: 357

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    
    total = 10
    unique_digits = 9
    current_available_digits = 9
    
    while n > 1 and current_available_digits > 0:
        unique_digits *= current_available_digits
        total += unique_digits
        current_available_digits -= 1
        n -= 1
        
    return total


## Structure
def countNumbersWithUniqueDigits(n):
    # Your code here

    pass