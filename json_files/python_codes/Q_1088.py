##Question ID: 1088

def confusingNumberII(n):
    def helper(current):
        nonlocal count, validNums
        for num in validNums:
            next_num = current * 10 + num
            if next_num > n:
                break
            if current != 0 or next_num != 0:
                if next_num != rotate(next_num):
                    count += 1
                count = helper(next_num)
        return count

    def rotate(num):
        rotated = 0
        original = num
        while num > 0:
            digit = num % 10
            if digit in (2, 3, 4, 5, 7):
                return original
            revd = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
            rotated = rotated * 10 + revd[digit]
            num //= 10
        return rotated

    count = 0
    validNums = [0, 1, 6, 8, 9]
    return helper(0)

## Structure
def confusingNumberII(n):
    # Your code here

    pass