##Question ID: 269

from collections import deque, defaultdict, Counter

def alienOrder(words):
    graph = defaultdict(set)
    in_degree = Counter({c: 0 for word in words for c in word})
    
    for word1, word2 in zip(words, words[1:]):
        found = False
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                found = True
                break
        if not found and len(word1) > len(word2):
            return ""
    
    q = deque([c for c in in_degree if in_degree[c] == 0])
    result = []
    while q:
        c = q.popleft()
        result.append(c)
        
        for neigh in graph[c]:
            in_degree[neigh] -= 1
            if in_degree[neigh] == 0:
                q.append(neigh)
                 
    if len(result) < len(in_degree):
        return ""
    
    return "".join(result)

## Structure
from collections import deque, defaultdict, Counter
    # Your code here

    pass