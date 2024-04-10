##Question ID: 1153

def canConvert(str1, str2):
    if str1 == str2: return True;
    conversion = {}
    for c1, c2 in zip(str1, str2):
        if c1 in conversion and conversion[c1] != c2: return False
        conversion[c1] = c2
    return len(set(str2)) < 26


## Structure
def canConvert(str1, str2):
    # Your code here

    pass