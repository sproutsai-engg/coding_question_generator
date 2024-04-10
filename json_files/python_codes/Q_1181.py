##Question ID: 1181

from collections import defaultdict

def beforeAndAfterPuzzles(phrases):
    first_word_map = defaultdict(set)
    result = set()

    for phrase in phrases:
        first_word = phrase.split(' ')[0]
        first_word_map[first_word].add(phrase)

    for phrase in phrases:
        last_word = phrase.split(' ')[-1]
        if last_word in first_word_map:
            for cur_phrase in first_word_map[last_word]:
                if phrase != cur_phrase:
                    result.add(phrase + cur_phrase[cur_phrase.index(' '):])

    return sorted(list(result))

## Structure
from collections import defaultdict
    # Your code here

    pass