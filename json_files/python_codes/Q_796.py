##Question ID: 796

def can_transform(sx, sy, tx, ty):
    while sx != tx or sy != ty:
        if sx > tx or sy > ty:
            return False
        if sx < tx:
            tx -= ty
        else:
            ty -= sx
    return True

## Structure
def can_transform(sx, sy, tx, ty):
    # Your code here

    pass