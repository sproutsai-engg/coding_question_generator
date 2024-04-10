##Question ID: 795

def kthSymbolInGrammar(n, k):
    if n == 1:
        return 0
    if k % 2 == 0:
        return 1 - kthSymbolInGrammar(n - 1, k // 2)
    else:
        return kthSymbolInGrammar(n - 1, (k + 1) // 2)

## Structure
def kthSymbolInGrammar(n, k):
    # Your code here

    pass