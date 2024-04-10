##Question ID: 544

def findContestMatch(n):
    matches = [str(i) for i in range(1, n + 1)]

    while n > 1:
        for i in range(n // 2):
            matches[i] = "(" + matches[i] + "," + matches[n - 1 - i] + ")"
        n //= 2

    return matches[0]


## Structure
def findContestMatch(n):
    # Your code here

    pass