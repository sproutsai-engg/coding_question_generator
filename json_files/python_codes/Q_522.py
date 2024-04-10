##Question ID: 522

def find_lus_length(strs):
    max_length = -1
    for i in range(len(strs)):
        is_uncommon = True
        for j in range(len(strs)):
            if i != j and strs[i] in strs[j]:
                is_uncommon = False
                break
        if is_uncommon:
            max_length = max(max_length, len(strs[i]))
    return max_length


## Structure
def find_lus_length(strs):
    # Your code here

    pass