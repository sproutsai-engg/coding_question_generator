##Question ID: 890

def lemonadeChange(bills):
    five, ten = 0, 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if not five:
                return False
            five -= 1
            ten += 1
        else:
            if ten and five:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True

## Structure
def lemonadeChange(bills):
    # Your code here

    pass