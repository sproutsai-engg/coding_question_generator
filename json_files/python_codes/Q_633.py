##Question ID: 633

def judge_square_sum(c):
    for a in range(int(c ** 0.5) + 1):
        b = int((c - a * a) ** 0.5)
        if a * a + b * b == c:
            return True
    return False

## Structure
def judge_square_sum(c):
    # Your code here

    pass