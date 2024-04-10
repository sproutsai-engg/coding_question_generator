##Question ID: 855

def count_unique_chars(s):
    return len(set(s))

def sum_count_unique_chars(s):
    sum = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sum += count_unique_chars(s[i:j])
    return sum

## Structure
def count_unique_chars(s):
    # Your code here

    pass