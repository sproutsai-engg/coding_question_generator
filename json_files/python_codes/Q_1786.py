##Question ID: 1786

def count_consistent_strings(allowed, words):
    allowed_set = set(allowed)
    count = 0
    for word in words:
        is_valid = True
        for c in word:
            if c not in allowed_set:
                is_valid = False
                break
        if is_valid:
            count += 1
    return count

## Structure
def count_consistent_strings(allowed, words):
    # Your code here

    pass