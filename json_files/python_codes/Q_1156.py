##Question ID: 1156

def find_third_words(text, first, second):
    words = text.split()
    result = []
    
    for i in range(len(words) - 2):
        if words[i] == first and words[i + 1] == second:
            result.append(words[i + 2])
            
    return result

## Structure
def find_third_words(text, first, second):
    # Your code here

    pass