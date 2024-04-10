##Question ID: 1933

def num_different_integers(word):
    for c in word:
        if not c.isdigit():
            word = word.replace(c, ' ')
    nums = word.split()
    unique_nums = set()
    for num in nums:
        num = num.lstrip('0') or '0'
        unique_nums.add(num)
    return len(unique_nums)

## Structure
def num_different_integers(word):
    # Your code here

    pass