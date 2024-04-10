##Question ID: 383

def can_construct(ransom_note, magazine):
    letter_count = {}
    
    for c in magazine:
        letter_count[c] = letter_count.get(c, 0) + 1
        
    for c in ransom_note:
        if c not in letter_count or letter_count[c] == 0:
            return False
        letter_count[c] -= 1
        
    return True

## Structure
def can_construct(ransom_note, magazine):
    # Your code here

    pass