##Question ID: 500

def find_words(words):
    rows = [
        set("qwertyuiopQWERTYUIOP"),
        set("asdfghjklASDFGHJKL"),
        set("zxcvbnmZXCVBNM")
    ]
    res = []

    for word in words:
        row = -1
        for i in range(3):
            if word[0] in rows[i]:
                row = i
                break

        if all(c in rows[row] for c in word):
            res.append(word)

    return res


## Structure
def find_words(words):
    # Your code here

    pass