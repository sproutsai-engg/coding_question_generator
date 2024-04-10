##Question ID: 1363

from collections import defaultdict

def largest_multiple_of_three(digits):
    digits.sort(reverse=True)
    sum_digits = sum(digits)

    if sum_digits % 3 == 0:
        return '0' if digits[-1] == 0 else ''.join(map(str, digits))

    mod = defaultdict(list)
    for digit in digits:
        mod[digit % 3].append(digit)

    if sum_digits % 3 == 1:
        if mod[1]:
            mod[1].pop()
        else:
            mod[2].pop(), mod[2].pop()
    else:
        if mod[2]:
            mod[2].pop()
        else:
            mod[1].pop(), mod[1].pop()

    result = "".join(str(digit) for value in mod.values() for digit in value)
    result = "".join(sorted(result, reverse=True))

    return '0' if not result or result[0] == '0' else result


## Structure
from collections import defaultdict
    # Your code here

    pass