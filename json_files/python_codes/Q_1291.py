##Question ID: 1291

def sequential_digits(low, high):
    result = []
    for i in range(1, 10):
        number = i
        for j in range(i + 1, 10):
            number = number * 10 + j
            if low <= number <= high:
                result.append(number)
    return sorted(result)

## Structure
def sequential_digits(low, high):
    # Your code here

    pass