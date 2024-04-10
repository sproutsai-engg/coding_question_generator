##Question ID: 873

import random

def match(a, b):
    return sum(a[i] == b[i] for i in range(6))

def find_secret_word(wordlist, master):
    for _ in range(10):
        guess = random.choice(wordlist)
        match_cnt = master.guess(guess)
        if match_cnt == 6:
            return
        wordlist = [word for word in wordlist if match(word, guess) == match_cnt]

## Structure
import random
    # Your code here

    pass