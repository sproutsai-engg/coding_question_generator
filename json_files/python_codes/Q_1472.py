##Question ID: 1472

from collections import OrderedDict

def sortString(s: str) -> str:
    freq_map = OrderedDict(sorted({c: s.count(c) for c in set(s)}.items()))
    result = []

    while freq_map:
        for key in list(freq_map.keys()):
            result.append(key)
            freq_map[key] -= 1

            if freq_map[key] == 0:
                del freq_map[key]

        for key in list(reversed(freq_map.keys())):
            result.append(key)
            freq_map[key] -= 1

            if freq_map[key] == 0:
                del freq_map[key]

    return "".join(result)

## Structure
from collections import OrderedDict
    # Your code here

    pass