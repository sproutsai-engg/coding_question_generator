##Question ID: 800

def letterCasePermutation(s):
    def backtrack(index):
        if index == len(s):
            result.append("".join(s))
            return
        backtrack(index + 1)
        if s[index].isalpha():
            s[index] = s[index].swapcase()
            backtrack(index + 1)
            s[index] = s[index].swapcase()

    result = []
    s = list(s)
    backtrack(0)
    return result

## Structure
def letterCasePermutation(s):
    # Your code here

    pass