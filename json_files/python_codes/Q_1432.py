##Question ID: 1432

def max_diff(num):
    a, b = -1, -1
    num_str = str(num)
    for c in num_str:
        if a == -1 and c != '9':
            a = int(c)
        if b == -1 and c > '1':
            b = int(c)
        if a != -1 and b != -1:
            break
            
    result = 0
    for c in num_str:
        if int(c) == a:
            result = result * 10 + 9
        elif int(c) == b:
            result = result * 10 + (1 if c == num_str[0] else 0)
        else:
            result = result * 10 + int(c)
    return result - num


## Structure
def max_diff(num):
    # Your code here

    pass