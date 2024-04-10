##Question ID: 1006

def spellchecker(wordlist, queries):
    word_map = {word: word for word in wordlist}
    word_map_lower_case = {word.lower(): word for word in wordlist if word.lower() not in word_map_lower_case}
    word_map_vowel_replaced = {replace_vowels(word.lower()): word for word in wordlist if replace_vowels(word.lower()) not in word_map_vowel_replaced}

    result = []
    for query in queries:
        lower_query = query.lower()
        vowel_replaced_query = replace_vowels(lower_query)

        if query in word_map:
            result.append(word_map[query])
        elif lower_query in word_map_lower_case:
            result.append(word_map_lower_case[lower_query])
        elif vowel_replaced_query in word_map_vowel_replaced:
            result.append(word_map_vowel_replaced[vowel_replaced_query])
        else:
            result.append("")

    return result


def replace_vowels(word):
    return ''.join(['#' if ch in 'aeiou' else ch for ch in word])


## Structure
def spellchecker(wordlist, queries):
    # Your code here

    pass