##Question ID: 678

def checkValidString(s: str) -> bool:
    left_balance, right_balance = 0, 0

    for i in range(len(s)):
        left_balance += 1 if s[i] == '(' or s[i] == '*' else -1
        right_balance += 1 if s[len(s) - 1 - i] == ')' or s[len(s) - 1 - i] == '*' else -1

        if left_balance < 0 or right_balance < 0:
            return False

    return True


## Structure
def checkValidString(s: str) -> bool:
    # Your code here

    pass