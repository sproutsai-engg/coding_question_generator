##Question ID: 1743

def count_substrings_with_one_difference(s, t):
    count = 0
    for i in range(len(s)):
        for j in range(len(t)):
            differences = 0
            k = 0
            while i + k < len(s) and j + k < len(t):
                if s[i + k] != t[j + k]:
                    differences += 1
                if differences == 2:
                    break
                if differences == 1:
                    count += 1
                k += 1
    return count

## Structure
def count_substrings_with_one_difference(s, t):
    # Your code here

    pass