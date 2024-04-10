##Question ID: 929

def num_special_equivalent_groups(words):
    groups = set()

    for word in words:
        evens = "".join(sorted(word[0::2]))
        odds = "".join(sorted(word[1::2]))

        groups.add(evens + odds)

    return len(groups)


## Structure
def num_special_equivalent_groups(words):
    # Your code here

    pass