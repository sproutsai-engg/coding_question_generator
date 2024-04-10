##Question ID: 749

def shortest_completing_word(license_plate, words):
    target = [0] * 26
    for c in license_plate:
        if c.isalpha():
            target[ord(c.lower()) - ord('a')] += 1

    result = ""
    for word in words:
        current = [0] * 26
        for c in word:
            if c.isalpha():
                current[ord(c.lower()) - ord('a')] += 1

        if all(a <= b for a, b in zip(target, current)) and (not result or len(word) < len(result)):
            result = word

    return result

## Structure
def shortest_completing_word(license_plate, words):
    # Your code here

    pass