##Question ID: 271

def encode(strs):
    encoded_string = ""
    for s in strs:
        encoded_string += str(len(s)) + "#" + s
    return encoded_string

def decode(s):
    strs = []
    i = 0
    while i < len(s):
        delimiter_pos = s.find('#', i)
        length = int(s[i:delimiter_pos])
        strs.append(s[delimiter_pos + 1:delimiter_pos + 1 + length])
        i = delimiter_pos + 1 + length
    return strs


## Structure
def encode(strs):
    # Your code here

    pass