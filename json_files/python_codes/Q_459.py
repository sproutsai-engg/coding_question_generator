##Question ID: 459

def can_construct(s):
    n = len(s)
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            substr = s[:i]
            flag = True
            for j in range(i, n, i):
                if s[j:j+i] != substr:
                    flag = False
                    break

            if flag:
                return True

    return False


## Structure
def can_construct(s):
    # Your code here

    pass