##Question ID: 1735

MOD = 10**9 + 7

def mul(a, b):
    return (a * b) % MOD

def ways(n, k, mem):
    if n == 1:
        return k
    if (n_tuple := (n, k)) in mem:
        return mem[n_tuple]
    if k == 1:
        mem[n_tuple] = 1
        return 1
    if n > k:
        mem[n_tuple] = 0
        return 0
    res = mul(ways(n, k - 1, mem), n)
    res = (res - mul(n - 1, ways(n - 1, k - 1, mem)) + MOD) % MOD
    mem[n_tuple] = res
    return res

def waysToFillArray(queries):
    mem = {}
    ans = []
    for q in queries:
        ans.append(ways(q[0], q[1], mem))
    return ans

## Structure
MOD = 10**9 + 7
    # Your code here

    pass