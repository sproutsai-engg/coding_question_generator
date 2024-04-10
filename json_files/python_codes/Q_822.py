##Question ID: 822

def uniqueMorseRepresentations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    transformations = set()

    for word in words:
        morseCode = ''.join(morse[ord(c) - ord('a')] for c in word)
        transformations.add(morseCode)

    return len(transformations)

## Structure
def uniqueMorseRepresentations(words):
    # Your code here

    pass