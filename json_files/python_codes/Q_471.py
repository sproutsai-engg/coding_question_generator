##Question ID: 471

def encode(s: str) -> str:
    n = len(s)
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            reps = n // i
            sub = s[:i]
            composed = sub * reps
            if s == composed:
                return f"{reps}[{sub}]"
    return s

## Structure
def encode(s: str) -> str:
    # Your code here

    pass