##Question ID: 245

def shortest_distance(words_dict, word1, word2):
    index1, index2, min_distance = -1, -1, float('inf')
    for i, word in enumerate(words_dict):
        if word == word1:
            index1 = i
        if word == word2:
            index2 = i
        if index1 != -1 and(index2 != -1):
            min_distance = min(min_distance, abs(index1 - index2))
    return min_distance

## Structure
def shortest_distance(words_dict, word1, word2):
    # Your code here

    pass