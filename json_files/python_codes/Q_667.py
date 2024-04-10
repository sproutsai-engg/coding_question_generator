##Question ID: 667

def constructArray(n: int, k: int) -> List[int]:
    answer = [0] * n
    for i in range(n):
        if i % 2 == 0:
            answer[i] = i // 2 + 1
        else:
            answer[i] = n - (i - 1) // 2
            k -= 1
    if k > 0:
        for i in range(n - 2, -1, -1):
            if k > 0:
                answer[i] = answer[i + 1] - answer[i]
                k -= 1
    return answer

## Structure
def constructArray(n: int, k: int) -> List[int]:
    # Your code here

    pass