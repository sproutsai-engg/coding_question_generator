##Question ID: 1049

def min_rotations(tops, bottoms):
    res = float('inf')

    for target in (tops[0], bottoms[0]):
        top_rot, bot_rot = 0, 0
        for ti, bi in zip(tops, bottoms):
            if ti != target and bi != target:
                top_rot = bot_rot = float('inf')
                break
            top_rot += ti != target
            bot_rot += bi != target

        res = min(res, top_rot, bot_rot)

    return -1 if res == float('inf') else res

## Structure
def min_rotations(tops, bottoms):
    # Your code here

    pass