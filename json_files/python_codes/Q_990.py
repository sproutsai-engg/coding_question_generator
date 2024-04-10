##Question ID: 990

def is_alien_sorted(words, order):
    alien_order = {char: i for i, char in enumerate(order)}

    for i in range(1, len(words)):
        for j in range(len(words[i - 1])):
            if j == len(words[i]):
                return False

            if words[i - 1][j] != words[i][j]:
                if alien_order[words[i - 1][j]] > alien_order[words[i][j]]:
                    return False
                break

    return True

## Structure
def is_alien_sorted(words, order):
    # Your code here

    pass