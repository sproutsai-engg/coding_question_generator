##Question ID: 482

def license_key_formatting(s: str, k: int) -> str:
    result = []
    count = 0
    for c in reversed(s):
        if c != '-':
            if count == k:
                result.append('-')
                count = 0
            result.append(c.upper())
            count += 1
    return ''.join(reversed(result))

## Structure
def license_key_formatting(s: str, k: int) -> str:
    # Your code here

    pass