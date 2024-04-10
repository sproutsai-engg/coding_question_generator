##Question ID: 1923

def are_sentences_similar(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()

    while words1 and words2 and words1[0] == words2[0]:
        words1.pop(0)
        words2.pop(0)
    
    while words1 and words2 and words1[-1] == words2[-1]:
        words1.pop()
        words2.pop()

    return not words1 or not words2

## Structure
def are_sentences_similar(sentence1, sentence2):
    # Your code here

    pass