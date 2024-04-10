##Question ID: 1273

def countSmallerFrequencies(words, queries):
    freqWords = [word.count(min(word)) for word in words]
    
    ans = []
    for query in queries:
        freqQuery = query.count(min(query))
        ans.append(sum(f > freqQuery for f in freqWords))
        
    return ans

## Structure
def countSmallerFrequencies(words, queries):
    # Your code here

    pass