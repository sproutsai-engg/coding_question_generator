##Question ID: 65

import re

def is_number(s: str) -> bool:
    pattern = re.compile(r'^[-+]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(e[-+]?[0-9]+)?$')
    return bool(pattern.match(s))


## Structure
import re
    # Your code here

    pass