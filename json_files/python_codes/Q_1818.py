##Question ID: 1818

def max_points(s, x, y):
    points = 0
    s = list(s)
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            points += max(x, y)
            s[i] = '#'
    return points

## Structure
def max_points(s, x, y):
    # Your code here

    pass