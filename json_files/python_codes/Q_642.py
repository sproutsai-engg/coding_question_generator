##Question ID: 642

from typing import List
import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentence = ""
        self.times = 0

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.current = self.root
        self.search = ""
        
        for i in range(len(sentences)):
            self.insert(sentences[i], times[i])

    def insert(self, sentence: str, times: int):
        curr = self.root
        for c in sentence:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.sentence = sentence
        curr.times += times

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.insert(self.search, 1)
            self.search = ""
            self.current = self.root
            return []
        
        self.search += c
        if not self.current:
            return []
        
        if c not in self.current.children:
            self.current = None
            return []
        
        self.current = self.current.children[c]
        heap = []
        for child in self.current.children.values():
            if child.times:
                heapq.heappush(heap, (-child.times, child.sentence))
        
        res = []
        for _ in range(3):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])
        return res


## Structure
from typing import List
    # Your code here

    pass