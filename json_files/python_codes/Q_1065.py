##Question ID: 1065

def has_all_codes_in_range(s: str, n: int) -> bool:
    substrings = set()
    length = len(bin(n)) - 2
    for i in range(len(s) - length + 1):
        substrings.add(s[i:i + length])
    return len(substrings) == n


## Structure
def has_all_codes_in_range(s: str, n: int) -> bool:
    # Your code here

    pass