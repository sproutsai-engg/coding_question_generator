##Question ID: 1297

def maxNumberOfBalloons(text):
    freqs = [0] * 26
    for c in text:
        freqs[ord(c) - ord('a')] += 1
    subs = [freqs[ord('b') - ord('a')], freqs[ord('a') - ord('a')], freqs[ord('l') - ord('a')] // 2, freqs[ord('o') - ord('a')] // 2, freqs[ord('n') - ord('a')]]
    return min(subs)


## Structure
def maxNumberOfBalloons(text):
    # Your code here

    pass