##Question ID: 1910

def check_ones_segment(s: str) -> bool:
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            if i > 0 and s[i - 1] == '0':
                count += 1
    return count <= 1

## Structure
def check_ones_segment(s: str) -> bool:
    # Your code here

    pass