##Question ID: 524

def findLongestWord(s, dictionary):
    def is_subsequence(target, source):
        iter_source = iter(source)
        return all(char in iter_source for char in target)

    dictionary = sorted(dictionary)
    longest = ''
    for word in dictionary:
        if is_subsequence(word, s) and len(word) > len(longest):
            longest = word
    return longest


## Structure
def findLongestWord(s, dictionary):
    # Your code here

    pass