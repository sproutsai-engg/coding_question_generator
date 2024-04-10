##Question ID: 465

from collections import defaultdict

def minTransfers(transactions):
    balances = defaultdict(int)
    for transaction in transactions:
        balances[transaction[0]] -= transaction[2]
        balances[transaction[1]] += transaction[2]

    debts = [balance for balance in balances.values() if balance != 0]
    return dfs(debts, 0)

def dfs(debts, start):
    while start < len(debts) and debts[start] == 0:
        start += 1
    if start == len(debts):
        return 0
    result = float('inf')
    for i in range(start + 1, len(debts)):
        if (debts[start] > 0) != (debts[i] > 0):
            debts[i] += debts[start]
            result = min(result, 1 + dfs(debts, start + 1))
            debts[i] -= debts[start]
    return result


## Structure
from collections import defaultdict
    # Your code here

    pass