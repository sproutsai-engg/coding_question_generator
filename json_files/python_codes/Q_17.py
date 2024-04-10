##Question ID: 17

def letter_combinations(digits: str):
    if not digits: return []
    phone = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    result = [""]

    for digit in digits:
        temp = []
        for s in result:
            for c in phone[int(digit) - 2]:
                temp.append(s + c)
        result = temp

    return result

## Structure
def letter_combinations(digits: str):
    # Your code here

    pass