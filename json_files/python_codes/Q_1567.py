##Question ID: 1567

def max_vowels(s, k):
    max_count = count = 0
    for i, c in enumerate(s):
        count += int(c in 'aeiou')
        if i >= k:
            count -= int(s[i - k] in 'aeiou')
        max_count = max(max_count, count)
    return max_count


## Structure
def max_vowels(s, k):
    # Your code here

    pass