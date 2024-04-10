##Question ID: 1219

def longest_wpi(hours):
    score = 0
    max_length = 0
    first_occurrence = {}

    for i, h in enumerate(hours):
        score += 1 if h > 8 else -1
        if score > 0:
            max_length = i + 1
        else:
            if score not in first_occurrence:
                first_occurrence[score] = i
            if score - 1 in first_occurrence:
                max_length = max(max_length, i - first_occurrence[score - 1])
    return max_length


## Structure
def longest_wpi(hours):
    # Your code here

    pass