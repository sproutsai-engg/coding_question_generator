##Question ID: 880

def rectangleArea(rectangles):
    mod = 10**9 + 7
    X = sorted(set(x for rect in rectangles for x in rect[::2]))
    Xdict = {x:i for i,x in enumerate(X)}

    events = []
    for x1,y1,x2,y2 in rectangles:
        events.append((Xdict[x1], 1, y1, y2))
        events.append((Xdict[x2], -1, y1, y2))
    events.sort()

    area = 0
    cnt = [0] * len(X)
    active = 0
    for idx, type, y1, y2 in events:
        area = (area + (X[idx+1] - X[idx]) * active % mod) % mod
        cnt[y1] += type
        cnt[y2] -= type
        active = sum(p for j,p in zip(X, cnt) if p)

    return area

## Structure
def rectangleArea(rectangles):
    # Your code here

    pass