##Question ID: 66

def plusOne(digits: List[int]) -> List[int]:
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    digits.insert(0, 1)
    return digits


## Structure
def plusOne(digits: List[int]) -> List[int]:
    # Your code here

    pass