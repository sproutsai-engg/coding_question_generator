##Question ID: 648

def replaceWords(dict, sentence):
    roots = set(dict)
    words = sentence.split()
    result = []

    for word in words:
        prefix = ''
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if prefix in roots:
                break
        result.append(prefix)

    return ' '.join(result)

## Structure
def replaceWords(dict, sentence):
    # Your code here

    pass