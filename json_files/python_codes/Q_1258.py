##Question ID: 1258

from typing import List


def generateSentences(synonyms: List[List[str]], text: str) -> List[str]:
    synonym_map = {}

    for s, t in synonyms:
        if s not in synonym_map:
            synonym_map[s] = {s}
        if t not in synonym_map:
            synonym_map[t] = {t}
        synonym_map[s].add(t)
        synonym_map[t].add(s)

    words = text.split()
    results = []

    def helper(index: int, cur_sentence: List[str]) -> None:
        if index == len(words):
            results.append(" ".join(cur_sentence))
            return
        for w in synonym_map.get(words[index], {words[index]}):
            cur_sentence.append(w)
            helper(index + 1, cur_sentence)
            cur_sentence.pop()

    helper(0, [])

    return sorted(results)


## Structure
from typing import List
    # Your code here

    pass