##Question ID: 926

def find_and_replace_patterns(words, pattern):
    result = []
    for word in words:
        if len(word) != len(pattern): continue

        w2p = {}
        p2w = {}
        matches = True
        for cWord, cPattern in zip(word, pattern):
            if cWord not in w2p: w2p[cWord] = cPattern
            if cPattern not in p2w: p2w[cPattern] = cWord

            if w2p[cWord] != cPattern or p2w[cPattern] != cWord:
                matches = False
                break

        if matches: result.append(word)
    return result


## Structure
def find_and_replace_patterns(words, pattern):
    # Your code here

    pass