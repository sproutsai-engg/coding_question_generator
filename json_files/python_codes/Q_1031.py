##Question ID: 1031

def add_to_array_form(num, k):
    for i in range(len(num) - 1, -1, -1):
        k, num[i] = divmod(num[i] + k, 10)
        if k == 0:
            break
    while k:
        k, digit = divmod(k, 10)
        num.insert(0, digit)
    return num


## Structure
def add_to_array_form(num, k):
    # Your code here

    pass