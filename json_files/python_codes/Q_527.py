##Question ID: 527

def wordsAbbreviation(words):
    def abbrev(word, k):
        return word[:k+1] + str(len(word) - k - 2) + word[-1] if k < len(word) - 2 else word

    n = len(words)
    abbr = [abbrev(word, 1) for word in words]
    prefix_len = [1] * n

    for i in range(n):
        while abbr.count(abbr[i]) > 1:
            groups = {}
            for j in range(i + 1, n):
                if abbr[i] == abbr[j]:
                    if abbr[j] not in groups:
                        groups[abbr[j]] = []
                    groups[abbr[j]].append(j)
            for group_members in groups.values():
                for j in group_members:
                    abbr[j] = abbrev(words[j], prefix_len[j] + 1)
                    prefix_len[j] += 1
            abbr[i] = abbrev(words[i], prefix_len[i] + 1)
            prefix_len[i] += 1

    return abbr

## Structure
def wordsAbbreviation(words):
    # Your code here

    pass