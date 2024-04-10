##Question ID: 418

def words_typing(sentence, rows, cols):
    total_chars = sum(len(word) + 1 for word in sentence)

    result = 0
    index = 0
    for _ in range(rows):
        remaining_cols = cols
        while True:
            word_len = len(sentence[index])
            if remaining_cols >= word_len:
                remaining_cols -= word_len + 1
                index = (index + 1) % len(sentence)
                if index == 0:
                    result += 1
            else:
                break

    return result

## Structure
def words_typing(sentence, rows, cols):
    # Your code here

    pass