##Question ID: 1061

def lex_smallest_equivalent(s1, s2, base_str):
    parent = {chr(ch): chr(ch) for ch in range(ord('a'), ord('z') + 1)}

    for c1, c2 in zip(s1, s2):
        root1, root2 = c1, c2
        while parent[root1] != root1:
            root1 = parent[root1]
        while parent[root2] != root2:
            root2 = parent[root2]
        if root1 != root2:
            min_root = min(root1, root2)
            parent[root1] = min_root
            parent[root2] = min_root

    return ''.join(parent[ch] for ch in base_str)

## Structure
def lex_smallest_equivalent(s1, s2, base_str):
    # Your code here

    pass