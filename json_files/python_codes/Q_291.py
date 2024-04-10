##Question ID: 291

def wordPatternMatch(pattern: str, s: str) -> bool:
    def backtrack(p_index, s_index, pattern_map, words):
        if p_index == len(pattern) and s_index == len(s):
            return True
        if p_index == len(pattern) or s_index == len(s):
            return False

        p = pattern[p_index]
        if p in pattern_map:
            word = pattern_map[p]
            if not s.startswith(word, s_index):
                return False
            return backtrack(p_index + 1, s_index + len(word), pattern_map, words)
        else:
            for length in range(1, len(s) - s_index + 1):
                word = s[s_index : s_index + length]
                if word in words:
                    continue
                pattern_map[p] = word
                words.add(word)
                if backtrack(p_index + 1, s_index + length, pattern_map, words):
                    return True
                pattern_map.pop(p)
                words.remove(word)
        return False

    return backtrack(0, 0, {}, set())

## Structure
def wordPatternMatch(pattern: str, s: str) -> bool:
    # Your code here

    pass