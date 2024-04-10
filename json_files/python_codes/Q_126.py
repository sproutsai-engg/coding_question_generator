##Question ID: 126

from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    wordList = set(wordList)
    if endWord not in wordList:
        return []

    adjacent = defaultdict(list)
    distance = defaultdict(int)
    queue = deque([beginWord])
    distance[beginWord] = 0
    
    def neighbors(word):
        for i in range(len(word)):
            for j in range(ord('a'), ord('z') + 1):
                yield word[:i] + chr(j) + word[i + 1:]
                
    while queue:
        current = queue.popleft()
        if current == endWord:
            break
        for neighbor in neighbors(current):
            if neighbor not in wordList:
                continue
            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
            if distance[neighbor] == distance[current] + 1:
                adjacent[current].append(neighbor)

    result = []
    path = [beginWord]

    def backtrack(word):
        if word == endWord:
            result.append(path[:])
        else:
            for next_word in adjacent[word]:
                path.append(next_word)
                backtrack(next_word)
                path.pop()
                
    backtrack(beginWord)
    return result


## Structure
from collections import defaultdict, deque
    # Your code here

    pass