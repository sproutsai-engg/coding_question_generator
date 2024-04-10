##Question ID: 1178

def find_num_of_valid_words(words, puzzles):
    result = []
    for puzzle in puzzles:
        count = 0
        puzzle_set = set(puzzle)
        for word in words:
            if puzzle[0] in word:
                if all(c in puzzle_set for c in word):
                    count += 1
        result.append(count)
    return result


## Structure
def find_num_of_valid_words(words, puzzles):
    # Your code here

    pass