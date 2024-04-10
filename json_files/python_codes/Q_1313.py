##Question ID: 1313

MOD = 10**9 + 7

def add_rooms(idx, children, memo):
    if not children[idx]:
        return 1
    if memo[idx] != -1:
        return memo[idx]

    res = 1
    cnt = 0
    for child in children[idx]:
        cnt += 1
        res = (res * add_rooms(child, children, memo)) % MOD
    
    for i in range(2, cnt + 1):
        res = (res * i) % MOD
    
    memo[idx] = res
    return res

def num_of_ways(prev_room):
    n = len(prev_room)
    children = [[] for _ in range(n)]
    for i in range(1, n):
        children[prev_room[i]].append(i)

    memo = [-1] * n
    return add_rooms(0, children, memo)

## Structure
MOD = 10**9 + 7
    # Your code here

    pass