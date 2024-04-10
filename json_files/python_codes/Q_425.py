##Question ID: 425

from collections import defaultdict

def wordSquares(words):
    def build(row, squares, word_lens):
        if row == word_lens:
            res.append(list(squares))
            return
        prefix = ''.join(squares[i][row] for i in range(row))
        for w in prefixes[prefix]:
            squares[row] = w
            build(row+1, squares, word_lens)

    if not words: return []
    res = []
    word_lens = len(words[0])
    
    prefixes = defaultdict(list)
    for word in words:
        for i in range(word_lens+1):
            prefixes[word[:i]].append(word)
            
    for word in words:
        build(1, [word] + [None]*(word_lens-1), word_lens)
        
    return res

## Structure
from collections import defaultdict
    # Your code here

    pass