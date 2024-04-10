##Question ID: 942

def isPalindrome(num):
    return str(num) == str(num)[::-1]

def superpalindromesInRange(left: str, right: str) -> int:
    l = int(left)
    r = int(right)
    cnt = 0
    base = 1
    while base * base <= r:
        if isPalindrome(base) and isPalindrome(base * base):
            if base * base >= l:
                cnt += 1
        base += 1
    return cnt


## Structure
def isPalindrome(num):
    # Your code here

    pass