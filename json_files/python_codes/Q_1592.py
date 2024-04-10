##Question ID: 1592

def reorderSpaces(text):
    spaces = text.count(' ')
    words = text.split()
    num_words = len(words)
    
    if num_words == 1:
        spaces_between_words = 0
    else:
        spaces_between_words = spaces // (num_words - 1)
    
    extra_spaces = spaces - spaces_between_words * (num_words - 1)

    return (' ' * spaces_between_words).join(words) + ' ' * extra_spaces

## Structure
def reorderSpaces(text):
    # Your code here

    pass