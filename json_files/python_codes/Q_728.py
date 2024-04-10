##Question ID: 728

def is_self_dividing(num):
    n = num
    while n:
        digit = n % 10
        if digit == 0 or num % digit != 0:
            return False
        n //= 10
    return True

def self_dividing_numbers(left, right):
    return [i for i in range(left, right+1) if is_self_dividing(i)]

## Structure
def is_self_dividing(num):
    # Your code here

    pass