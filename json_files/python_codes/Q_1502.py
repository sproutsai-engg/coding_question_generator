##Question ID: 1502

def can_construct(s, k):
    char_counts = [0] * 26

    for c in s:
        char_counts[ord(c) - ord('a')] += 1

    odd_count = sum(count % 2 for count in char_counts)

    return odd_count <= k <= len(s)


## Structure
def can_construct(s, k):
    # Your code here

    pass