##Question ID: 194

def transpose(content):
    data = [line.split(" ") for line in content]
    result = [" ".join(data[j][i] for j in range(len(data))) for i in range(len(data[0]))]
    return result


## Structure
def transpose(content):
    # Your code here

    pass