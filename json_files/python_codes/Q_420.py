##Question ID: 420

def strong_password(password):
    missing_lower = 1
    missing_upper = 1
    missing_digit = 1
    total = len(password)
    
    for c in password:
        if c.islower(): missing_lower = 0
        if c.isupper(): missing_upper = 0
        if c.isdigit(): missing_digit = 0
    
    missing = missing_lower + missing_upper + missing_digit
    if total < 6: return max(missing, 6 - total)
    if total > 20: return missing + total - 20

    return missing

## Structure
def strong_password(password):
    # Your code here

    pass