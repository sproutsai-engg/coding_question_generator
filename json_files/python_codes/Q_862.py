##Question ID: 862

def findReplaceString(s, indices, sources, targets):
    index_mapping = sorted(
        [(indices[i], i) for i in range(len(indices)) if s.startswith(sources[i], indices[i])]
    )
    result = []
    last_idx = 0

    for idx, i in index_mapping:
        result.append(s[last_idx:idx])
        result.append(targets[i])
        last_idx = idx + len(sources[i])

    result.append(s[last_idx:])
    return "".join(result)

## Structure
def findReplaceString(s, indices, sources, targets):
    # Your code here

    pass