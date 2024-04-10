##Question ID: 470

def rand7():
    pass  # Provided API

def rand10():
    result = None
    while True:
        result = (rand7() - 1) * 7 + rand7()
        if result <= 40:
            break
    return result % 10 + 1

## Structure
def rand7():
    # Your code here

    pass