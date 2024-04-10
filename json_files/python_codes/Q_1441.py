##Question ID: 1441

def build_array(target, n):
    result = []
    current = 1
    for num in target:
        while current < num:
            result.append("Push ")
            result.append("Pop ")
            current += 1
        result.append("Push ")
        current += 1
    return result

## Structure
def build_array(target, n):
    # Your code here

    pass