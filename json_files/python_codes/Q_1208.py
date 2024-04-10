##Question ID: 1208

def split_string(seq: str):
    result = [0] * len(seq)
    count = 0

    for i in range(len(seq)):
        if seq[i] == '(':
            result[i] = count % 2
            count += 1
        else:
            count -= 1
            result[i] = count % 2

    return result


## Structure
def split_string(seq: str):
    # Your code here

    pass