##Question ID: 1277

def largest_multiple_of_three(digits):
    count = [0] * 3
    num_sum = sum(digits)
    
    for d in digits:
        count[d % 3] += 1

    if num_sum % 3 == 1:
        if count[1] >= 1:
            count[1] -= 1
        else:
            count[2] -= 2
    elif num_sum % 3 == 2:
        if count[2] >= 1:
            count[2] -= 1
        else:
            count[1] -= 2

    res = ""
    for i in range(10):
        res += str(i) * count[i % 3]
    
    if res and res[-1] == "0":
        return "0"
    return res[::-1]

## Structure
def largest_multiple_of_three(digits):
    # Your code here

    pass