##Question ID: 737

from collections import defaultdict

def areSentencesSimilar(sentence1, sentence2, pairs):
    if len(sentence1) != len(sentence2):
        return False
    
    graph = defaultdict(set)
    for a, b in pairs:
        graph[a].add(b)
        graph[b].add(a)

    for a, b in zip(sentence1, sentence2):
        if a == b:
            continue
        if b not in graph[a]:
            return False

    return True

## Structure
from collections import defaultdict
    # Your code here

    pass