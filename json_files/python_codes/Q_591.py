##Question ID: 591

def is_valid(code, i):
    if i >= len(code) or code[i] != '<':
        return False, i
    i += 1
    name_start = i
    while i < len(code) and code[i].isupper():
        i += 1
    name_len = i - name_start
    if name_len < 1 or name_len > 9 or code[i] != '>':
        return False, i
    i += 1

    while i < len(code) and code[i] != '<':
        i += 1
    if i + 2 + name_len >= len(code) or code[i:i + 2 + name_len] != '</' + code[name_start:i] + '>':
        return False, i
    return True, i + 2 + name_len

def validate_code_snippet(code):
    is_valid_code, i = is_valid(code, 0)
    return is_valid_code and i == len(code)

## Structure
def is_valid(code, i):
    # Your code here

    pass