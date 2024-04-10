##Question ID: 1714

def reorder_spaces(text: str) -> str:
    spaces = text.count(' ')
    words = text.split()
    
    if len(words) == 1:
        return words[0] + ' ' * spaces

    space_between_words = spaces // (len(words) - 1)
    extra_spaces = spaces % (len(words) - 1)
    result = ''
    
    for i, word in enumerate(words):
        result += word
        if i < len(words) - 1:
            result += ' ' * space_between_words
    
    result += ' ' * extra_spaces

    return result

## Structure
def reorder_spaces(text: str) -> str:
    # Your code here

    pass