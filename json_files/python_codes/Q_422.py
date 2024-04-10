##Question ID: 422

def valid_word_square(words):
    for i in range(len(words)):
        for j in range(len(words[i])):
            if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                return False
    return True


## Structure
def valid_word_square(words):
    # Your code here

    pass