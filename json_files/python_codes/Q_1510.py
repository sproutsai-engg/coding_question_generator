##Question ID: 1510

def find_lucky(arr):
    freq = {}

    for n in arr:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    lucky = -1
    for key, value in freq.items():
        if key == value:
            lucky = max(lucky, key)

    return lucky

## Structure
def find_lucky(arr):
    # Your code here

    pass