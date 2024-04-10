##Question ID: 1530

def check_if_can_break(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    can_break_1 = can_break_2 = True
    for c1, c2 in zip(s1, s2):
        if c1 < c2:
            can_break_1 = False
        if c2 < c1:
            can_break_2 = False

    return can_break_1 or can_break_2


## Structure
def check_if_can_break(s1, s2):
    # Your code here

    pass