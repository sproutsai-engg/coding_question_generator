##Question ID: 734

from collections import defaultdict

def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2): return False
    similarityMap = defaultdict(set)
    for pair in similarPairs:
        similarityMap[pair[0]].add(pair[1])
        similarityMap[pair[1]].add(pair[0])
    for i in range(len(sentence1)):
        if sentence1[i] != sentence2[i] and sentence2[i] not in similarityMap[sentence1[i]]:
            return False
    return True


## Structure
from collections import defaultdict
    # Your code here

    pass