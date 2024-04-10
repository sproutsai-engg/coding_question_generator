##Question ID: 345

def reverseVowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    s_list = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s_list[i] not in vowels:
            i += 1
        elif s_list[j] not in vowels:
            j -= 1
        else:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
    return ''.join(s_list)

## Structure
def reverseVowels(s: str) -> str:
    # Your code here

    pass