##Question ID: 1012

def isRationalEqual(s: str, t: str) -> bool:
    def evaluate(s: str) -> float:
        i = s.find('(')
        if i != -1:
            base = s[:i]
            rep = s[i + 1:-1]
            return float(base + rep * 20)
        return float(s)

    return abs(evaluate(s) - evaluate(t)) < 1e-12

## Structure
def isRationalEqual(s: str, t: str) -> bool:
    # Your code here

    pass