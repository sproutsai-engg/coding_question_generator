##Question ID: 968

def beautifulArray(n: int) -> List[int]:
    result = [1]
    while len(result) < n:
        temp = []
        for i in result:
            if i * 2 - 1 <= n:
                temp.append(i * 2 - 1)
        for i in result:
            if i * 2 <= n:
                temp.append(i * 2)
        result = temp
    return result

## Structure
def beautifulArray(n: int) -> List[int]:
    # Your code here

    pass