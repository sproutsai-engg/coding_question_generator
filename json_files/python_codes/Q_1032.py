##Question ID: 1032

def equationsPossible(equations):
    parent = [i for i in range(26)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for e in equations:
        if e[1] == '=':
            x = ord(e[0]) - ord('a')
            y = ord(e[3]) - ord('a')
            parent[find(x)] = find(y)

    for e in equations:
        if e[1] == '!' and find(ord(e[0]) - ord('a')) == find(ord(e[3]) - ord('a')):
            return False

    return True


## Structure
def equationsPossible(equations):
    # Your code here

    pass