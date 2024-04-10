##Question ID: 205

def is_isomorphic(s: str, t: str) -> bool:
    map1, map2 = {}, {}
    for char_s, char_t in zip(s, t):
        if char_s not in map1:
            map1[char_s] = char_t
        if char_t not in map2:
            map2[char_t] = char_s
        if map1[char_s] != char_t or map2[char_t] != char_s:
            return False
    return True

## Structure
def is_isomorphic(s: str, t: str) -> bool:
    # Your code here

    pass