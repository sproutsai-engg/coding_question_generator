##Question ID: 756

def pyramid_transition(bottom, allowed):
    mapping = {}
    for s in allowed:
        key = s[:2]
        if key not in mapping:
            mapping[key] = []
        mapping[key].append(s[2])
    return pyramid_transition_helper(bottom, "", 0, mapping)

def pyramid_transition_helper(bottom, top, idx, mapping):
    if len(bottom) == 1:
        return True
    if idx == len(bottom) - 1:
        return pyramid_transition_helper(top, "", 0, mapping)
    key = bottom[idx:idx + 2]
    if key not in mapping:
        return False
    for c in mapping[key]:
        if pyramid_transition_helper(bottom, top + c, idx + 1, mapping):
            return True
    return False


## Structure
def pyramid_transition(bottom, allowed):
    # Your code here

    pass