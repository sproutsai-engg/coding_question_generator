##Question ID: 455

def find_content_children(g, s):
    g.sort()
    s.sort()
    i = j = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1

        j += 1

    return i


## Structure
def find_content_children(g, s):
    # Your code here

    pass