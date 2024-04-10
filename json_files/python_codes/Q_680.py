##Question ID: 680

def validPalindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            temp1, temp2 = i + 1, j
            while temp1 < temp2 and s[temp1] == s[temp2]:
                temp1 += 1
                temp2 -= 1
            if temp1 >= temp2:
                return True

            temp1, temp2 = i, j - 1
            while temp1 < temp2 and s[temp1] == s[temp2]:
                temp1 += 1
                temp2 -= 1
            if temp1 >= temp2:
                return True

            return False
        i += 1
        j -= 1
    return True

## Structure
def validPalindrome(s: str) -> bool:
    # Your code here

    pass