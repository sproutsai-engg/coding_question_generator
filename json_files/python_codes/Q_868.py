##Question ID: 868

def push_dominoes(dominoes: str) -> str:
    prev, cur = None, dominoes
    while prev != cur:
        prev = cur
        cur_lst = list(prev)
        for i in range(len(cur)):
            if prev[i] == 'L' and i > 0 and prev[i - 1] == '.':
                cur_lst[i - 1] = 'L'
            elif prev[i] == 'R' and i < len(cur) - 1 and prev[i + 1] == '.':
                cur_lst[i + 1] = 'R'
        cur = ''.join(cur_lst)
    return cur

## Structure
def push_dominoes(dominoes: str) -> str:
    # Your code here

    pass