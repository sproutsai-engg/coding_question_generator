##Question ID: 424

def characterReplacement(s:str, k:int) -> int:
    n = len(s)
    left = 0
    right = 0
    maxFreq = 0
    result = 0
    freq = [0] * 26

    for right in range(n):
        freq[ord(s[right]) - ord('A')] += 1
        maxFreq = max(maxFreq, freq[ord(s[right]) - ord('A')])

        if right - left + 1 - maxFreq > k:
            freq[ord(s[left]) - ord('A')] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


## Structure
def characterReplacement(s:str, k:int) -> int:
    # Your code here

    pass