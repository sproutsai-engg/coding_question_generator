##Question ID: 1417

from collections import deque

def reformat(s: str) -> str:
    letters, digits = deque(), deque()

    for c in s:
        if c.isalpha():
            letters.append(c)
        else:
            digits.append(c)

    if abs(len(letters) - len(digits)) > 1:
        return ""

    result = []
    use_letter = len(letters) > len(digits)

    while letters or digits:
        if use_letter:
            result.append(letters.popleft())
        else:
            result.append(digits.popleft())
        use_letter = not use_letter

    return ''.join(result)

## Structure
from collections import deque
    # Your code here

    pass