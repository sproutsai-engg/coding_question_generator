##Question ID: 187

from collections import defaultdict

def findRepeatedDnaSequences(s: str):
    dna_counter = defaultdict(int)
    result = []

    for i in range(len(s) - 9):
        sequence = s[i:i + 10]
        dna_counter[sequence] += 1
        if dna_counter[sequence] == 2:
            result.append(sequence)

    return result

## Structure
from collections import defaultdict
    # Your code here

    pass