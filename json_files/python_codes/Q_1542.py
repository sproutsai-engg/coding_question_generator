##Question ID: 1542

def max_power(s: str) -> int:
    max_power = current_power = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_power += 1
        else:
            max_power = max(max_power, current_power)
            current_power = 1

    return max(max_power, current_power)

## Structure
def max_power(s: str) -> int:
    # Your code here

    pass