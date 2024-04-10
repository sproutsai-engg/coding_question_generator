##Question ID: 1557

def has_all_codes(s, k):
    need = 1 << k
    got = set()
    
    for i in range(len(s) - k + 1):
        got.add(s[i:i + k])
    
    return len(got) == need


## Structure
def has_all_codes(s, k):
    # Your code here

    pass