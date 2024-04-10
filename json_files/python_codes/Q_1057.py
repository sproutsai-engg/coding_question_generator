##Question ID: 1057

def num_dup_digits_at_most_n(n):
    count = 0
    for i in range(1, n + 1):
        digits = set()
        num = i
        while num != 0:
            digit = num % 10
            if digit in digits:
                count += 1
                break
            else:
                digits.add(digit)
            num //= 10
    return count

## Structure
def num_dup_digits_at_most_n(n):
    # Your code here

    pass